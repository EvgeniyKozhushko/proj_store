# Generated by Django 3.2.3 on 2021-06-28 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_statusorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='position', to='orders.statusorder'),
        ),
    ]
