from django import forms
from . import models



class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = ('phone_number', 'country', 'city', 'index', 'adress1', 'adress1', 'discription')    

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'    



# class CreateMyUserForm(forms.ModelForm):
#     class Meta:
#         model = models.MyUser
#         fields = ('username', 'password', 'email', 'first_name', 'last_name', 'phone_number', 'discription')  