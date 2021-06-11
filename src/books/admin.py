from django.contrib import admin

# Register your models here.
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title_book', 'book_price', 'date_inclusion']

admin.site.register(models.Book, BookAdmin)