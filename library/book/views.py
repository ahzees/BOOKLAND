# Create your views here.
from django.shortcuts import render, redirect

from author.models import Author
from book.forms import BookForm
from book.models import Book


def view_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    authors = book.authors.all()
    return render(request, 'authentication/view_book.html', {'book': book, 'authors': authors, 'title': book.name})


def library(request):
    if request.user.is_authenticated:
        posts = Book.objects.all()
        if request.method == 'POST':
            if request.POST.get('q'):
                try:
                    value = request.POST.get('q')
                    dict_filter = {'Book Name': Book.objects.filter(name__icontains=value)}
                    try:
                        dict_filter['Author Name'] = Author.objects.filter(name=value.split()[0],
                                                                           surname=value.split()[1]).first().books.all()
                        return render(request, 'authentication/library.html',
                                      {'posts': dict_filter[request.POST.get('filter')]})
                    except:
                        try:
                            try:
                                dict_filter['Book id'] = [Book.objects.get(pk=value)]
                                return render(request, 'authentication/library.html',
                                              {'posts': dict_filter[request.POST.get('filter')]})
                            except:
                                dict_filter['Author id'] = Author.objects.filter(pk=value).first().books.all()
                                return render(request, 'authentication/library.html',
                                              {'posts': dict_filter[request.POST.get('filter')]})
                        except:
                            return render(request, 'authentication/library.html',
                                          {'posts': dict_filter[request.POST.get('filter')]})
                except:
                    return render(request, 'authentication/library.html', {'posts': posts, 'error': 'Invalid name'})
        return render(request, 'authentication/library.html', {'posts': posts})
    else:
        return redirect('login')


def add_book(request):
    if request.user.role:
        if request.method == 'POST':
            form=BookForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'authentication/add_book.html',
                              {'success': 'The book has been added successfully',
                               'book': Book.objects.get(
                                   description=form.cleaned_data[
                                       'description'])})
        return render(request, 'authentication/add_book.html', {'form': BookForm()})
    else:
        return redirect('home')
