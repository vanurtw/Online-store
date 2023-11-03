from django import template
from cart.models import Cart

register = template.Library()


@register.inclusion_tag('cart/nocart.html')
def no_cart():
    return {}


@register.simple_tag(name='count')
def count(user):
    cart = Cart.objects.filter(user=user)
    count = cart.count()

    return count
