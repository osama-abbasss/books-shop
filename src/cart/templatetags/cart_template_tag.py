from django import template
from cart.models import Order

register = template.Library()


@register.filter
def cart_item_number(user):
    if user.is_authenticated:
        order_qs = Order.objects.filter(user=user, ordered=False)
        if order_qs.exists():
            return order_qs[0].products.count()
        else:
            return 0
    else:
        return 0
