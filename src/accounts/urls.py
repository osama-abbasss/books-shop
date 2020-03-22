from django.urls import path
from . import views

app_name = 'profile'


urlpatterns = [
    path('track/orders/', views.user_orders , name='orders')
]
