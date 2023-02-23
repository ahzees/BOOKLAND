from django.urls import path

from author.views import *

urlpatterns = [
    path('add_author/', add_author, name='add_author'),
    path('all_author/',all_author,name='all_authors'),
    path('view_author/<int:author_id>/',view_author,name='view_author'),
    path('delete_author/<int:author_id>/',delete_author,name='delete_author'),
]