from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def profile_contents(request):
    """ Display the user's profile. """
    if request.user.is_anonymous:
        is_author = False
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        is_author = profile.is_author

    context = {
        #'form': form,
        # 'orders': orders,
        'is_author': is_author,
        'on_profile_page': False
    }

    return context
