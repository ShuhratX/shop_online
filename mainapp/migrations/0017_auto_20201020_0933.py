# Generated by Django 3.1.2 on 2020-10-20 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20201018_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='final_price',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='final_price',
        ),
    ]
