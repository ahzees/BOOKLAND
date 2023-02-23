from django.urls import path

from authentication.views import index, login_view, register, logout_view, my_profile, \
    user, all_users, close_order

#
urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('my_profile/', my_profile, name='my_profile'),
    path('register/', register, name='register'),
    path('user/<int:user_id>/', user, name='user'),
    path('all_users/', all_users, name='all_users'),
    path('close_order/<int:order_id>/',close_order,name='close_order')
]