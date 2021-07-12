from django.contrib import admin

# Register your models here.
from . import models

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'phone_number','country', 'city', 'index', 'adress1', 'adress1', 'discription']  

admin.site.register(models.Customer, CustomerAdmin)