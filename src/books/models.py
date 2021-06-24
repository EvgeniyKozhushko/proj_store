from django.db import models
from django.urls import reverse
from catalogs.models import Author, Genre, Series, PublishingHouse

# Create your models here.

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
    in_stock = models.IntegerField(verbose_name="Количество в наличии")
    available_to_order = models.BooleanField(verbose_name="Доступна к заказу", default=True)
    rating = models.IntegerField(verbose_name="Рейтинг (0-10)", blank=True, null=True)
    date_inclusion = models.DateTimeField(verbose_name="Дата внесения в каталог", auto_now_add=True, auto_now=False)
    date_change = models.DateTimeField(verbose_name="Дата последнего изменения карточки", auto_now_add=False, auto_now=True)

    def __str__(self) -> str:
        return f"{self.title_book}"

    def get_absolute_url(self):
        return reverse('books:book-list')
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"