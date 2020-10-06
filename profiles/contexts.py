from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def profile_contents(request):
    """ Display the user's profile. """
    chapterOrders=[]
    if request.user.is_anonymous:
        is_author = False
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        is_author = profile.is_author
        chapterOrders = profile.chapter_orders.all()

    context = {
        #'form': form,
        'chapterOrders': chapterOrders,
        'is_author': is_author,
        'on_profile_page': False
    }

    return context
