from django.urls import path

from book.views import *

urlpatterns = [
    path('library/', library, name='library'),
    path('library/view/<int:book_id>/', view_book, name='view'),
    path('add_book/', add_book, name='add_book'),
]