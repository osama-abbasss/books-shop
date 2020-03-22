from django.urls import path
from . import views


app_name= 'products'

urlpatterns = [
    path('', views.products_view , name='list'),
    path('<slug>/', views.product_detail_view, name='detail'),

]
