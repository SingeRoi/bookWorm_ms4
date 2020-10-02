from django.urls import path
from . import views
from bookCoins.views import buy_chapter

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<product_id>/<chapter_id>', views.chapter, name='chapter'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('buy_chapter', buy_chapter, name='buy_chapter'),
]

