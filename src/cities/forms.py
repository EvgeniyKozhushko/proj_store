from django import forms
from . import models

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = '__all__'

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = '__all__'

class CreatePublishingHouseForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = '__all__'        