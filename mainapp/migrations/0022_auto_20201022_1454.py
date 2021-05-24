# Generated by Django 3.1.2 on 2020-10-22 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_auto_20201020_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Ism')),
                ('last_name', models.CharField(max_length=255, verbose_name='Familiya')),
                ('phone', models.CharField(max_length=25, verbose_name='Tel raqam')),
                ('address', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Manzil')),
                ('status', models.CharField(choices=[('new', 'Yangi buyurtma'), ('in_progress', 'Buyurtma tayyorlanmoqda'), ('ready', 'Buyurtma tayyor'), ('completed', 'Buyurtma bajarildi')], default='new', max_length=100, verbose_name='Buyurtma holati')),
                ('buying_type', models.CharField(choices=[('self', 'Olib ketish'), ('delivery', 'Yetkazib berish')], default='self', max_length=100, verbose_name='Buyurtma turi')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Buyurtma haqida izoh')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Buyurtma qilingan vaqt')),
                ('order_date', models.DateField(default=django.utils.timezone.now, verbose_name='Buyurtma qabul qilingan vaqt')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Mijoz')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='Mijoz buyurtmalari'),
        ),
    ]
