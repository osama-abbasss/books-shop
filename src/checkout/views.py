from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CheckoutForm
from .models import Address
from cart.models import Order
import string
import random


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=25))

def checkout_view(request):

#---#POST
    if request.method == 'POST':
        form = CheckoutForm(request.POST or None)
        order = Order.objects.get(user= request.user, ordered=False)
        if form.is_valid():
            # useing degault billing address
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            default_billing = request.POST.get('default_billing_address')
            ship_diffrent_address = request.POST.get('ship_diffrent_address')
            if default_billing:
                billing_address = Address.objects.filter(user=request.user,
                                                        default_address=True,
                                                        address_type='B').last()
                order.billing_address = billing_address
                if not ship_diffrent_address:
                    order.shipping_address = billing_address
                order.code = create_ref_code()
                order.ordered = True
                order.in_way = True
                order.save()
            else:

                #new billing address
                billing_country = request.POST.get("billing_country")
                address = request.POST.get("address")
                zip_code = request.POST.get("zip_code")
                phone_num = request.POST.get("phone_num")

                new_billing_address = Address(
                                    user = request.user,
                                    first_name = first_name,
                                    last_name = last_name,
                                    country = billing_country,
                                    zip_code = zip_code,
                                    address = address,
                                    address_type = 'B',
                                    phone_num = phone_num,
                                    )
                new_billing_address.save()
                set_billing_default = request.POST.get("set_billing_address")
                if set_billing_default:
                    new_billing_address.default_address = True
                    new_billing_address.save()
                order.billing_address = new_billing_address
                if not ship_diffrent_address:
                    order.shipping_address = new_billing_address
                order.code = create_ref_code()
                order.ordered = True
                order.in_way = True
                order.save()

            # shipping address not billing address

            set_shipping_address = request.POST.get('set_shipping_address')
            default_shipping_address = request.POST.get('default_shipping_address')
            if ship_diffrent_address:
                first_name_s = request.POST.get("first_name_s")
                last_name_s = request.POST.get("last_name_s")
                #use default shipping address
                if default_shipping_address:
                    shipping_address = Address.objects.filter(user=request.user,
                                                            default_address=True,
                                                            address_type='S').last()
                    order.shipping_address = shipping_address
                    order.code = create_ref_code()
                    order.ordered = True
                    order.in_way = True
                    order.save()
                else:
                    #new shipping address
                    shipping_country = request.POST.get("shipping_country")
                    shipping_address = request.POST.get("shipping_address")
                    shipping_zip_code = request.POST.get("shipping_zip_code")
                    shipping_phone = request.POST.get("shipping_phone")

                    new_Shipping_address = Address(
                                        user = request.user,
                                        first_name = first_name_s,
                                        last_name = last_name_s,
                                        country = shipping_country,
                                        zip_code = shipping_zip_code,
                                        address = shipping_address,
                                        address_type = 'S',
                                        phone_num = shipping_phone,
                                        )
                    new_Shipping_address.save()
                    if set_shipping_address:
                        new_shipping_address.default_address = True
                        new_shipping_address.save()
                    order.shipping_address = new_Shipping_address
                    order.code = create_ref_code()
                    order.ordered = True
                    order.in_way = True
                    order.save()

            messages.info(request, 'success')
            return redirect("/")
        else:
            messages.info(request, 'sorry someyhing is wrong try again')
            return redirect("checkout:checkout")


#---# GET
    else:
        try:
            order = Order.objects.get(user= request.user, ordered=False)
            form  = CheckoutForm()
            context = {'form':form,
                        'order':order
                        }
        except:
            messages.info(request, 'sorry you dont have any active order')
            return redirect("products:list")

        #get default billing
        last_default_billing_address = Address.objects.filter(user= request.user,
                                                    address_type='B',
                                                default_address=True)
        if last_default_billing_address.exists():
            context.update({'default_billing_address':last_default_billing_address.last()})

        #get default shipping
        last_default_shipping_address = Address.objects.filter(user= request.user,
                                                    address_type='S',
                                                default_address=True)
        if last_default_shipping_address.exists():
            context.update({'default_shipping_address':last_default_shipping_address.last()})


    template_name = 'checkout/checkout.html'

    return render(request, template_name, context)
