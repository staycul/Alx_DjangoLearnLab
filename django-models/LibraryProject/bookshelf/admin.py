from django.contrib import admin
from .models import Book

# Customize how Book appears in the admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # shows these fields in the list view
    search_fields = ('title', 'author')                     # adds a search box for title/author
    list_filter = ('publication_year',)                     # adds filter sidebar for publication_year
