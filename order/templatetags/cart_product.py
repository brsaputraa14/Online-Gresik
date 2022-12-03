from django import template
from django.shortcuts import HttpResponse
from order.models import Cart , Order

register = template.Library()

@register.filter
def cart_view(user):
    cart = Cart.objects.filter(user=user, purchased=False)

    if cart.exists():
        return cart
    else:
        return cart

@register.filter
def order_view(user):
    cart = Cart.objects.filter(user=user, purchased=False)
    post = Order.objects.filter(user=user,ordered=True).first()
    order = post.orderitems.all()   
    
    if order.exists():
        return order
    else:
        return order

@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].get_totals()

    else:
        return 0 

@register.filter
def cart_count(user):
    order = Order.objects.filter(user=user, ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0