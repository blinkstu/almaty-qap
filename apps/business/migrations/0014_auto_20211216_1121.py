# Generated by Django 3.2.9 on 2021-12-16 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0013_auto_20211216_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
    ]
