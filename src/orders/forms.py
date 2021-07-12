from django import forms
from django.db.models import fields
from . import models

class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label = 'Контактная инофрмация', required = True, widget=forms.TextInput)

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields='__all__'