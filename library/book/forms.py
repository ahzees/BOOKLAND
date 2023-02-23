from django import forms
from .models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count', 'year_of_publication', 'date_of_issue_of_the_book']
        widgets = {
            'description': forms.Textarea(
                attrs={'id': 'description', 'max_lenght': 256, 'placeholder': 'description'}),
            'year_of_publication': forms.DateTimeInput(format='%Y-%m-%d',
                                                       attrs={'class': 'form-control',
                                                              'placeholder': 'Select a date',
                                                              'type': 'date'
                                                              }),
            'date_of_issue_of_the_book': forms.DateTimeInput(format='%Y-%m-%d',
                                                             attrs={'class': 'form-control',
                                                                    'placeholder': 'Select a date',
                                                                    'type': 'date'
                                                                    })
        }
