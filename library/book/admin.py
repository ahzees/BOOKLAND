from django.contrib import admin

from author.models import Author
from .forms import BookForm
from .models import *


class AddAuthorsInline(admin.TabularInline):
    model = Author.books.through
    verbose_name = 'Автори'
    verbose_name_plural = 'Authors'
    extra = 0

    def has_add_permission(self, request, obj=None):
        if obj:
            return False
        else:
            return True

    def has_change_permission(self, request, obj = None):
        return False

    def has_delete_permission(self, request, obj = None):
        return False


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('name', 'description', 'year_of_publication', 'date_of_issue_of_the_book'),
    #     }),
    # )
    list_display = ('id', 'name', 'count', 'get_authors')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'authors__name', 'authors__surname')
    form = BookForm
    fieldsets = (
        ('Unchanged info', {
            'fields': ('name', 'year_of_publication')}),
        ('Changed info', {'fields': ('date_of_issue_of_the_book', 'description', 'count')}),
    )
    inlines = [
        AddAuthorsInline,
    ]

    list_filter = ('id', 'name', 'authors')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["name", "year_of_publication", ]
        else:
            return []

    def get_authors(self, args):
        return [i.name + ' ' + i.surname for i in args.authors.all()]
