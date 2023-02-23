# Create your views here.
import datetime

from django.shortcuts import redirect, render

from book.models import Book
from order.models import Order


def buy_book(request, book_id):
    if request.user.is_authenticated:
        user = request.user
        try:
            Order.create(user=user, book=Book.objects.get(pk=book_id))
            instance = Book.objects.get(pk=book_id)
            if instance.count > 1:
                count = instance.count - 1
                instance.update(count=count)
                return redirect(request.META.get('HTTP_REFERER'))

            else:
                return redirect(request.META.get('HTTP_REFERER'))
        except:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('login')


def delete_order(request, order_id):
    if request.user.is_authenticated and request.user.role == 1:
        x = Order.objects.get(pk=order_id)
        y = Book.objects.get(pk=x.book_id)
        y.update(count=y.count + 1)
        Order.objects.get(id=order_id).delete()

        return redirect(request.META.get('HTTP_REFERER'))


