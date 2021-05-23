# Generated by Django 3.2.3 on 2021-05-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_book', models.TextField(verbose_name='Название книги')),
                ('book_price', models.IntegerField(verbose_name='Цена книги(BYN)')),
                ('book_author', models.TextField(verbose_name='Автор книги')),
                ('book_series', models.TextField(verbose_name='Серия книги')),
                ('book_genre', models.TextField(verbose_name='Жанр книги')),
                ('year_publishing', models.IntegerField(verbose_name='Год издания')),
                ('number_pages', models.IntegerField(verbose_name='Количество страниц')),
                ('binding', models.TextField(verbose_name='Переплет')),
                ('size', models.TextField(verbose_name='Формат')),
                ('ISBN', models.TextField(verbose_name='ISNB')),
                ('age_restrictions', models.CharField(max_length=20, verbose_name='Возрастные ограничения')),
                ('publishing_house', models.TextField(verbose_name='Издательство')),
                ('weight', models.IntegerField(verbose_name='Вес (гр)')),
                ('in_stock', models.IntegerField(verbose_name='Количество в наличии')),
                ('available_to_order', models.BooleanField(default=True, verbose_name='Доступна к заказу')),
                ('rating', models.IntegerField(verbose_name='Рейтинг (0-10)')),
                ('date_inclusion', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в каталог')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения карточки')),
            ],
        ),
    ]
