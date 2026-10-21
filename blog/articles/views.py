from django.shortcuts import render
from django.http import Http404
from .models import Order


def archive(request):
    return render(request, 'archive.html', {"posts": Order.objects.all()})


def get_order(request, order_id):
    try:
        post = Order.objects.get(id=order_id)
        return render(request, 'order.html', {"post": post})
    except Order.DoesNotExist:
        raise Http404
