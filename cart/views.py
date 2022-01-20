import asyncio
import json

from asgiref.sync import sync_to_async
from django.conf.global_settings import LOGIN_URL
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from products.models import Book
# Create your views here.
from .models import Order, OrderItem


def get_cart_data(request):
    user = request.user
    order, created = asyncio.run(create_order(user))
    items = asyncio.run(get_all_order_items(order))
    cart_items = order.items_count
    return {'cart_items': cart_items, 'order': order, 'items': items}


@login_required(login_url=LOGIN_URL)
def index(request):
    data = get_cart_data(request)

    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cart_items': cart_items}
    return render(request, 'cart/index.html', context)


@login_required(login_url=LOGIN_URL)
def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    user = request.user
    product = asyncio.run(get_product(product_id))
    order, created = asyncio.run(create_order(user=user, complete=False))

    order_item, created = asyncio.run(create_order_item(order, product))

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        if order_item.quantity > 0:
            order_item.quantity -= 1
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


@login_required(login_url=LOGIN_URL)
def save_order(request):
    data = json.loads(request.body)
    order_id = data['orderId']
    action = data['action']

    order = asyncio.run(get_order(order_id))

    if action == 'save':
        order.complete = True
        order.save()
        messages.success(request, 'Order successfully created')

    return HttpResponse(status=200)


@sync_to_async
def get_product(product_id):
    return Book.objects.get(id=product_id)


@sync_to_async
def create_order(user, complete=False):
    return Order.objects.get_or_create(user=user, complete=complete)


@sync_to_async
def create_order_item(order, product):
    return OrderItem.objects.get_or_create(order=order, product=product)


@sync_to_async
def get_order(pk):
    return Order.objects.get(pk=pk)


@sync_to_async
def get_all_order_items(order):
    return order.orderitem_set.all()
