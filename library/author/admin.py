from django.contrib import admin

from .forms import AuthorForm
from .models import *


class BookInline(admin.TabularInline):
    model = Author.books.through
    verbose_name = 'Author`s book'
    extra = 0

    def has_change_permission(self, request, obj=None):
        return True


class AuthorAdmin(admin.ModelAdmin):
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('id', 'name', 'surname', 'patronymic',),
    #     }),
    # )
    #
    # fieldsets = (
    #     (None, {'fields': ('name', 'surname', 'patronymic')}),
    # )
    inlines = [
        BookInline,
    ]
    form = AuthorForm
    list_display = ['id', 'name', 'surname', 'get_books']
    list_display_links = ['id', 'name', 'surname', ]
    search_fields = ['id', 'name', 'books__name']

    def get_books(self, args):
        return [i.name for i in args.books.all()]


admin.site.register(Author, AuthorAdmin)
