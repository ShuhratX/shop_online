# Generated by Django 3.1.2 on 2020-10-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20201018_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=12, verbose_name='Umumiy narx'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=8, max_digits=12, verbose_name='Umumiy narx'),
        ),
    ]
