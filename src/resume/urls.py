from django.urls import path
from . import views


app_name= 'resume'
urlpatterns = [
    path('', views.sections_view, name='sections_list'),
    path('<slug>/',views.section_details_view, name='section_details')

]
