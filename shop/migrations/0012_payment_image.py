# Generated by Django 4.1.7 on 2023-05-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_product_type_mis'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Изображение'),
        ),
    ]
