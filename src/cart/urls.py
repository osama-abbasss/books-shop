from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add_item/<slug>/', views.add_item_to_cart, name='add_item'),
    path('remove_one_item/<slug>/', views.remove_one_item, name='remove_one_item'),
    path('remove_all_items/<slug>/', views.remove_all_items, name='remove_all_items'),
]
