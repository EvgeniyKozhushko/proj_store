from django.contrib import admin

# Register your models here.
from . import models

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user']  

admin.site.register(models.Employee, EmployeeAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'phone_number']  

admin.site.register(models.Customer, CustomerAdmin)


# admin.site.register(models.Customer, CustomerAdmin)

# class StaffAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'login', 'email']  

# admin.site.register(models.Staff, StaffAdmin)