from django.contrib import admin

from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book')
    list_display_links = ('id', 'user', 'book')
    search_fields = ('id','user__first_name','user__last_name','book__pk','book__name')
    sortable_by = ('id','book__pk','user__pk')

admin.site.register(Order, OrderAdmin)
