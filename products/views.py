from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Chapter, UserRatings
from profiles.models import UserProfile
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from .forms import ProductForm, UserRatingsForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(products, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    chapters = Chapter.objects.filter(book=product_id)
    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)
        try:
            rating = UserRatings.objects.get(book=product, user=user)
            rating_loop_times = range(1, int(rating.user_rating)+1)
        except UserRatings.DoesNotExist:
            rating_loop_times = 0
    else:
        rating_loop_times = 0

    context = {
        'product': product,
        'chapters': chapters,
        'ratingLoopTimes': rating_loop_times,
    }

    return render(request, 'products/product_detail.html', context)

def chapter(request, product_id, chapter_id):

    product = get_object_or_404(Product, pk=product_id)
    chapter = get_object_or_404(Chapter, pk=chapter_id)

    context = {
        'product': product,
        'chapter': chapter,
    }

    return render(request, 'products/chapter.html', context)

@login_required
def add_product(request):
    """Add a product to the store only as a superuser"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES )
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product! PLease ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    '''Edit a title in the store only as a superuser'''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product_id]))
        else:
            messages.error(request, 'Failed to update product! PLease ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing (product.name)')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    '''Delete a title from the store only as a superuser'''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Deleted title.')
    return redirect(reverse('products'))


@login_required
def rate_product(request, product_id):


    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    form_data = {
        'book': product,
        'user': user,
        'user_rating': request.POST['starinput'],
    }

    if request.method == "POST":
        form = UserRatingsForm(form_data)
        if form.is_valid():
            form.save()

    return redirect(reverse('product_detail', args=[product.id]))

"""
@login_required
def get_user_rating(request, product_id):
    Get user rating
    redirect_url = request.POST['redirect_url']
    book=get_object_or_404profcut,pk=product_id;
    if request.method == 'POST':
        form_data = {
            'user_rating': request.POST['starinput'],
            'user': request.user,
            book:book,
        }

        rating_form = UserRatingsForm(form_data)
        if rating_form.is_valid():
            order = rating_form.save()
            order.save()

            return redirect(redirect_url)
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    return redirect(redirect_url)
"""