from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    dim_1 = models.CharField(verbose_name='Выбор автора', max_length=60)
    author_discription = models.TextField(verbose_name= 'Описание', blank=True, null=True)
    picture_author = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/')

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
    picture_series = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/')

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
    picture_genre = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/')

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
    picture_publishing_house = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/')

    def __str__(self) -> str:
        return self.dim_4

    def get_absolute_url(self):
        return reverse('publishinghouse:published-list')
    class Meta:
        verbose_name = "Выбор издателя"
        verbose_name_plural = "Выбор издателя"   
class Book(models.Model):
    title_book = models.CharField(verbose_name="Название книги", max_length= 200)
    picture_book = models.ImageField(verbose_name="Картинка", upload_to = 'author/%Y/%m/%d/')
    book_price = models.IntegerField(verbose_name="Цена книги(BYN)")
    book_author = models.ManyToManyField(Author, related_name='authors') # должен быть справочник
    book_series = models.ForeignKey(Series, on_delete=models.PROTECT, related_name='series', blank=True, null=True) # должен быть справочник
    book_genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='genres') # должен быть справочник
    year_publishing = models.IntegerField(verbose_name= "Год издания")
    number_pages = models.IntegerField(verbose_name="Количество страниц")
    binding = models.CharField(verbose_name="Переплет",max_length= 100) # можно сделать справочик
    size = models.CharField(verbose_name="Формат", max_length= 100)
    ISBN = models.CharField(verbose_name="ISBN",max_length= 100)
    weight = models.IntegerField(verbose_name="Вес (гр)")
    age_restrictions = models.CharField(verbose_name="Возрастные ограничения",max_length=20)# можно сделать справочик
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.PROTECT, related_name='publishing_houses') # должен быть справочник
    weight = models.IntegerField(verbose_name="Вес (гр)")
    in_stock = models.IntegerField(verbose_name="Количество в наличии")
    available_to_order = models.BooleanField(verbose_name="Доступна к заказу", default=True)
    rating = models.IntegerField(verbose_name="Рейтинг (0-10)", blank=True, null=True)
    date_inclusion = models.DateTimeField(verbose_name="Дата внесения в каталог", auto_now_add=True, auto_now=False)
    date_change = models.DateTimeField(verbose_name="Дата последнего изменения карточки", auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return f"Наименование {self.title_book}"

    def get_absolute_url(self):
        return reverse('book:book-list')
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"