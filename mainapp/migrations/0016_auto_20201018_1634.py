# Generated by Django 3.1.2 on 2020-10-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20201018_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='final_price',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19, verbose_name='Umumiy narx'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Umumiy narx'),
        ),
    ]
