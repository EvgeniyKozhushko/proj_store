from django import forms
from . import models

class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(label = 'Контактная инофрмация', required = True, widget=forms.TextInput)