from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cart', 'status_order' , 'contact_info'] 


admin.site.register(models.Order, OrderAdmin)