# Generated by Django 3.1.2 on 2020-10-23 05:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Buyurtma qabul qilish vaqti'),
        ),
    ]
