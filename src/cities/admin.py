from django.contrib import admin

# Register your models here.

from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title_book', 'book_price', 'date_inclusion']
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dim_1']    
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dim_2'] 
class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dim_3']     
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dim_4'] 

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.PublishingHouse, PublishingHouseAdmin)
admin.site.register(models.Book, BookAdmin)