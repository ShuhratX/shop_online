# Generated by Django 3.1.2 on 2020-10-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20201018_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Umumiy narx'),
        ),
    ]