from django import forms

from book.models import Book
from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'patronymic',]


class AuthorToBook(forms.Form):
    authors = forms.ModelChoiceField(queryset=Author.objects.order_by('pk'))
    books = forms.ModelChoiceField(queryset=Book.objects.order_by('pk'))

