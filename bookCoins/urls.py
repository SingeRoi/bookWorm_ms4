from django.urls import path
from . import views
# from .webhooks import webhook

urlpatterns = [
    path('', views.topup_coins, name='topup_coins'),
    path('topup_success/<order_number>', views.topup_success, name='topup_success'),
]


"""urlpatterns = [
    
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
"""
