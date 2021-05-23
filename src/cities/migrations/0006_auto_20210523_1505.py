# Generated by Django 3.2.3 on 2021-05-23 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0005_alter_book_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim_3', models.CharField(max_length=60, verbose_name='Выбор жанра')),
            ],
            options={
                'verbose_name': 'Выбор жанра',
                'verbose_name_plural': 'Выбор жанра',
            },
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim_4', models.CharField(max_length=60, verbose_name='Выбор издателя')),
            ],
            options={
                'verbose_name': 'Выбор издателя',
                'verbose_name_plural': 'Выбор издателя',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dim_2', models.CharField(max_length=60, verbose_name='Выбор серии')),
            ],
            options={
                'verbose_name': 'Выбор серии',
                'verbose_name_plural': 'Выбор серии',
            },
        ),
        migrations.RenameField(
            model_name='author',
            old_name='dim',
            new_name='dim_1',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='cities.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='series', to='cities.series'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publishing_houses', to='cities.publishinghouse'),
        ),
    ]
