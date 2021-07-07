from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'cart', 'status_order' , 'contact_info'] 

# class StatusOrderAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'status'] 

# admin.site.register(models.StatusOrder, StatusOrderAdmin)    
admin.site.register(models.Order, OrderAdmin)