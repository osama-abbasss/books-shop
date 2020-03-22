from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from . import forms
from cart.models import Order



class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.UserCreateForm
    success_url="/accounts/login/"

@login_required
def user_orders(request):
    orders_qs = Order.objects.filter(user = request.user)

    template_name = 'profile/track_orders.html'

    context = {'orders':orders_qs}

    return render(request, template_name, context)
