# Create your views here.
from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, redirect

from author.forms import AuthorForm, AuthorToBook
from author.models import Author
from book.models import Book


def all_author(request):
    if request.user.is_authenticated and request.user.role == 1:
        if request.method == 'POST':
            return render(request, 'authentication/all_authors.html', {'authors': Author.get_all_0()})
        else:
            authors = Author.get_all()
            return render(request, 'authentication/all_authors.html', {'authors': authors})
    else:
        return redirect('home')


def view_author(request, author_id):
    return render(request, 'authentication/view_author.html', {'author': Author.objects.get(pk=author_id)})


def delete_author(request, author_id):
    Author.delete_by_id(author_id=author_id)
    return redirect('all_authors')


def add_author(request):
    if request.user.role:
        if request.method == 'POST':
            form1 = AuthorForm(request.POST)
            form2 = AuthorToBook(request.POST)
            if request.POST.get('authors') and request.POST.get('books'):
                try:
                    Book.objects.get(pk=request.POST.get('books')).add_authors(
                        [Author.objects.get(pk=request.POST.get('authors'))])
                    return redirect('add_author')
                except:
                    return render(request, 'authentication/add_author.html',
                                  {'error': 'Invalid data', 'form1': AuthorForm(), 'form2': AuthorToBook()})
            if request.POST.get('name') and request.POST.get('surname') and request.POST.get('patronymic'):
                try:
                    if Author.objects.filter(name=request.POST.get('name'), surname=request.POST.get('surname'),
                                             patronymic=request.POST.get('patronymic')):
                        raise MultipleObjectsReturned()
                    x = Author.create(name=request.POST.get('name'), surname=request.POST.get('surname'),
                                      patronymic=request.POST.get('patronymic'))

                except MultipleObjectsReturned:
                    return redirect('add_author')
                except:
                    return render(request, 'authentication/add_author.html',
                                  {'error': 'Invalid data', 'form1': AuthorForm(request.POST), 'form2': AuthorToBook()})
                else:
                    return redirect('add_author')
            return render(request, 'authentication/add_author.html', {'form1': AuthorForm(), 'form2': AuthorToBook()})
        else:
            return render(request, 'authentication/add_author.html', {'form1': AuthorForm(), 'form2': AuthorToBook()})
    else:
        redirect('home')
