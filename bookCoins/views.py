from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import OrderCoinForm, OrderChapterForm
from .models import OrderCoin, OrderChapter, OrderChapterLineItem

from products.models import Product, Chapter
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import json
import stripe


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)



@csrf_exempt
def update_coins(request):
    """ Add a quantity of the specified product to the shopping bag """
    redirect_url = request.POST.get('redirect_url')
    current_coin = request.POST.get('current_coin')
    if not request.POST.get('client_secret'):
        pid={}
    else:
        pid = request.POST.get('client_secret').split('_secret')[0]
    request.session['current_coin'] = current_coin
    request.session['pid'] = pid
    request.session.modified = True

    return redirect(redirect_url)


def topup_coins(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_coin = int(request.session.get('current_coin', 5))
    pid = request.session.get('pid')
    stripe_total = round(current_coin * 100)

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'coins': request.POST['coins'],
        }

        order_form = OrderCoinForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid_in_form = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid_in_form
            order.save()
            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('topup_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderCoinForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderCoinForm()
        else:
            order_form = OrderCoinForm()

    if not pid:
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        client_secret = intent.client_secret
    else:
        stripe.api_key = stripe_secret_key
        stripe.PaymentIntent.modify(pid, amount=stripe_total)
        client_secret = pid

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, 'bookCoins/topup_coins.html', context)



def topup_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(OrderCoin, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's coins
        coin_data = {
            'bookcoins': order.coins + profile.bookcoins,
        }
        user_coin_form = UserProfileForm(coin_data, instance=profile)
        if user_coin_form.is_valid():
            user_coin_form.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
                'bookcoins': profile.bookcoins,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'current_coin' in request.session:
        del request.session['current_coin']
    if 'pid' in request.session:
        del request.session['pid']

    context = {
        'order': order,
    }

    return render(request, 'bookCoins/topup_success.html', context)



def buy_chapter(request):
    """
    Buy chapters
    """

    if request.method == 'POST':

        chapterid = request.POST['chapterId']
        productid = request.POST['productId']

        profile = UserProfile.objects.get(user=request.user)
        chapter = get_object_or_404(Chapter, pk=chapterid)

        order_chapter_form_data = {
            'user_profile': profile,
        }

        order_chapter_form = OrderChapterForm(order_chapter_form_data)
        if order_chapter_form.is_valid():
            order = order_chapter_form.save()
            order_line_item = OrderChapterLineItem(
                order=order,
                chapter=chapter,
                chapter_no=chapter.chapter,
                book= chapter.book,
                lineitem_total=chapter.price,
            )
            order_line_item.save()
            # Attach the user's profile to the order
            order.user_profile = profile
            order.save()
        else:
            print("there's an error")
            print(order_chapter_form.errors)

        # Save the user's coins

        coin_data = {
            'bookcoins': profile.bookcoins - chapter.price,
        }
        user_coin_form = UserProfileForm(coin_data, instance=profile)
        if user_coin_form.is_valid():
            user_coin_form.save()

    """messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    """
    product = get_object_or_404(Product, pk=productid)
    chapters = Chapter.objects.filter(book=productid)

    context = {
        'product': product,
        'chapters':chapters,
    }

    return redirect(reverse('product_detail', args=[productid]))

