# Generated by Django 3.2.9 on 2021-12-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0010_auto_20211215_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]
