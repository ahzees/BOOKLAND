from django.urls import path

from order.views import *

urlpatterns = [
    path('buy_book/<int:book_id>/', buy_book, name='buy_book'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
]