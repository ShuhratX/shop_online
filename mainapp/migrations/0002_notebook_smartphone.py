# Generated by Django 3.1 on 2020-10-04 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nomi')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Rasm')),
                ('description', models.TextField(null=True, verbose_name='Tafsilotlar')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Narxi')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Displey turi')),
                ('resolution', models.CharField(max_length=255, verbose_name="Ekran o'lchamlari")),
                ('accum_volume', models.CharField(max_length=255, verbose_name='Akkumulyator hajmmi')),
                ('ram', models.CharField(max_length=255, verbose_name='Tezkor xotira')),
                ('sd', models.BooleanField(default=True)),
                ('sd_volume_max', models.CharField(max_length=255, verbose_name='Maksimal tashqi xotira')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='Asosiy kamera')),
                ('front_cam_mp', models.CharField(max_length=255, verbose_name='Frontal kamera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Kategoriya')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Nomi')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Rasm')),
                ('description', models.TextField(null=True, verbose_name='Tafsilotlar')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Narxi')),
                ('diagonal', models.CharField(max_length=255, verbose_name='Diagonal')),
                ('display_type', models.CharField(max_length=255, verbose_name='Displey turi')),
                ('processor_freq', models.CharField(max_length=255, verbose_name='Chastotasi')),
                ('ram', models.CharField(max_length=255, verbose_name='Tezkor xotira')),
                ('videokart', models.CharField(max_length=255, verbose_name='Videokarta')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='Akkumulyator ishlash vaqti')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Kategoriya')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]