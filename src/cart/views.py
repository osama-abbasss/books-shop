from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import CartItem, Order
from products.models import Product

def cart_view(request):
    order = get_object_or_404(Order, user =request.user, ordered=False)

    template_name = 'cart/cart.html'
    context = {
        'order':order
    }
    return render(request, template_name, context)





@login_required
def add_item_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)

    order_item, create = CartItem.objects.get_or_create(user= request.user, product=product)

    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.products.filter(product__slug= product.slug).exists():
            order_item.quantity +=1
            order_item.save()
            return redirect('cart:cart')
        else:
            order.products.add(order_item)
            order.save()
            return redirect('cart:cart')

    else:
        order = Order.objects.create(user=request.user)
        order.products.add(order_item)
        order.save()
        return redirect('cart:cart')


    return redirect('cart:cart')


@login_required
def remove_one_item(request, slug):
    product = get_object_or_404(Product, slug=slug)

    order_item = get_object_or_404(CartItem ,user= request.user, product=product)

    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.products.filter(product__slug= product.slug).exists:
            if order_item.quantity >1:
                order_item.quantity -=1
            else:
                order.products.remove(order_item)
            order_item.save()
            return redirect('cart:cart')
        else:

            return redirect('/')

    else:
        return redirect('/')

    return redirect('cart:cart')


@login_required
def remove_all_items(request, slug):
    product = get_object_or_404(Product, slug=slug)

    order_item = get_object_or_404(CartItem ,user= request.user, product=product)

    order_qs = Order.objects.filter(user= request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.products.filter(product__slug= product.slug).exists:
            order.products.remove(order_item)
            order_item.save()
            return redirect('cart:cart')
        else:

            return redirect('/')

    else:
        return redirect('/')

    return redirect('cart:cart')
