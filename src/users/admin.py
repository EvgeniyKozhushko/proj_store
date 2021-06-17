from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Employee)

# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'login', 'email']  

# admin.site.register(models.Customer, CustomerAdmin)

# class StaffAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'login', 'email']  

# admin.site.register(models.Staff, StaffAdmin)