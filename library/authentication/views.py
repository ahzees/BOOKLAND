import datetime

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse

from authentication.forms import *
from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


def index(request):
    return render(request, 'authentication/base.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def my_profile(request):
    if request.user.is_authenticated:
        lst = []
        dct = {}
        orders = Order.objects.filter(user_id=request.user.pk)
        for i in orders:
            lst.append(Book.objects.get(pk=i.book_id))
        for i in range(len(orders)):
            dct[orders[i]] = lst[i]
        return render(request, 'authentication/myprofile.html', {'dct': dct})
    else:
        return redirect('home')


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, username=email, password=password)
                if user is None:
                    context = {'error': 'Invalid email or  password', 'form': form}
                    return render(request, 'authentication/login.html', context)
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        return render(request, 'authentication/login.html', {'form': LoginForm()})
    else:
        return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            x = request.POST
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                return render(request, 'authentication/registration.html', {'error': 'Try again'})
    else:
        form = RegistrationForm()
    return render(request, 'authentication/registration.html', {'form': form})


def user(request, user_id):
    if request.user.is_authenticated and request.user.role == 1:
        user = CustomUser.objects.get(id=user_id)
        orders = Order.objects.filter(user_id=user_id)
        return render(request, 'authentication/user.html', {'orders': orders, 'user': user})
    else:
        return redirect('home')


def all_users(request):
    if request.user.is_authenticated and request.user.role == 1:
        if request.POST.get('q'):
            value = request.POST.get('q')
            dict_filter = {'User Name': CustomUser.objects.filter(first_name=value)}
            try:
                dict_filter['User id'] = CustomUser.objects.filter(pk=value)
            except:
                users = dict_filter[request.POST.get('filter')]
                return render(request, 'authentication/all_users.html', {'users': users})
            users = dict_filter[request.POST.get('filter')]
            return render(request, 'authentication/all_users.html', {'users': users})
        users = CustomUser.objects.filter(role=0)
        return render(request, 'authentication/all_users.html', {'users': users, 'Order': Order})
    else:
        return redirect('home')


def close_order(request, order_id):
    if request.user.role:
        if request.method == 'GET':
            try:
                Order.objects.get(id=order_id).update(end_at=datetime.datetime.now())
                return redirect(request.META.get('HTTP_REFERER'))
            except:
                redirect(request.META.get('HTTP_REFERER'))
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')
