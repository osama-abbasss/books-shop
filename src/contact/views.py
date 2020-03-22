from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

from cart.models import Order


def refund_request(request):

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            email = request.POST.get("email")
            order_code = request.POST.get("order_code")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            order = Order.objects.filter(user= request.user , ordered=True, code=order_code)
            if order.exists():
                order = Order.objects.get(user= request.user , ordered=True, code=order_code)
                contact = Contact(
                user = request.user,
                email = email,
                order_code = order_code,
                subject = subject,
                message = message
                )
                contact.save()
                order.refund_requested = True
                order.save()

                messages.info(request, 'thanks for contact us, we will response soon')
                return redirect("/")
            else:
                messages.info(request, 'we dont have any orders with this code')
                return redirect("contact:contact")
        else:
            messages.info(request, 'faild, try again')
            return redirect("contact:contact")
    else:
        form = ContactForm()

    template_name = 'contact/contact.html'
    context ={}
    return render(request, template_name, context)
