# Generated by Django 3.1 on 2020-10-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_notebook_smartphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
