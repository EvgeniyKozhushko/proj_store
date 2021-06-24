from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    dim_1 = models.CharField(verbose_name='Выбор автора', max_length=60)
    author_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)
    picture_author = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/',blank=True, null=True)

    def __str__(self) -> str:
        return self.dim_1

    def get_absolute_url(self):
        return reverse('author:author-list')

    class Meta:
        verbose_name = "Выбор автора"
        verbose_name_plural = "Выбор автора"
class Series(models.Model):
    dim_2 = models.CharField(verbose_name='Выбор серии', max_length=60)
    series_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)

    def __str__(self) -> str:
        return self.dim_2

    def get_absolute_url(self):
        return reverse('series:series-list')
    class Meta:
        verbose_name = "Выбор серии"
        verbose_name_plural = "Выбор серии"   
class Genre(models.Model):
    dim_3 = models.CharField(verbose_name='Выбор жанра', max_length=60)
    genre_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.dim_3

    def get_absolute_url(self):
        return reverse('genre:genre-list')    
    class Meta:
        verbose_name = "Выбор жанра"
        verbose_name_plural = "Выбор жанра"        
class PublishingHouse(models.Model):
    dim_4 = models.CharField(verbose_name='Выбор издателя', max_length=60)
    publishing_house_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.dim_4

    def get_absolute_url(self):
        return reverse('publishinghouse:published-list')
    class Meta:
        verbose_name = "Выбор издателя"
        verbose_name_plural = "Выбор издателя"   