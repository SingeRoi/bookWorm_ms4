from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from bookCoins.models import OrderCoin



@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.coin_orders.all()
    chapterOrders = profile.chapter_orders.all()
    context = {
        'orders': orders,
        'chapterOrders': chapterOrders,
        'profile': profile,
        'on_profile_page': True
    }
    '''do i need an if statement from profiles view.py?
        if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    '''
    return render(request, 'profiles/profile.html', context)

@login_required
def update_billing(request):
    """ Update User's billing address """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'on_profile_page': True
    }

    return render(request, 'profiles/update_billing.html', context)

@login_required
def order_history(request, order_number):
    orderCoin = get_object_or_404(OrderCoin, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': orderCoin,
        'from_profile': True,
    }

    return render(request, 'bookCoins/topup_success.html', context)