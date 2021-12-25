# Generated by Django 3.2.9 on 2021-12-15 16:42

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0007_auto_20211215_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='target',
        ),
        migrations.AddField(
            model_name='menu',
            name='open_on_new_tab',
            field=models.BooleanField(default=False, verbose_name='Открыть на новой вкладке браузера'),
        ),
        migrations.AddField(
            model_name='menu',
            name='to_page',
            field=models.BooleanField(default=False, verbose_name='Наведить на страницу'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='содержание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='содержание Казахский'),
        ),
    ]
