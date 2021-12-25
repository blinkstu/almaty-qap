import os
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.admin import display
from django.db import models
# Create your models here.
from django.template.loader import get_template
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from topnotchdev import files_widget


class Category(MPTTModel):
    name = models.CharField(verbose_name=_('Название'), max_length=255, unique=True)
    name_kk = models.CharField(verbose_name=_('Название Казахский'), max_length=255, null=True, blank=True)
    thumbnail = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    parent = TreeForeignKey('self', verbose_name=_('Категория родителей'), on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.CharField(verbose_name=_('Тип'), max_length=255, default='product', choices=[('product', _('Продукт')), ('page', _('Страница'))])

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


class Page(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    title_kk = models.CharField(max_length=255, verbose_name=_('Заголовок_kk'), null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True, verbose_name=_('содержание'))
    content_kk = RichTextUploadingField(blank=True, null=True, verbose_name=_('содержание Казахский'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Страница')
        verbose_name_plural = _('Страницы')


class Menu(MPTTModel):
    name = models.CharField(verbose_name=_('Название'), max_length=255, unique=True)
    name_kk = models.CharField(verbose_name=_('Название Казахский'), max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', verbose_name=_('Меню родителей'), on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    to_page = models.BooleanField(verbose_name=_('Наведить на страницу'), default=False)
    url = models.CharField(verbose_name=_('Ссылка'), null=True, blank=True, max_length=255)
    open_on_new_tab = models.BooleanField(verbose_name=_('Открыть на новой вкладке браузера'), default=False)
    slug = models.CharField(verbose_name=_('Тип'), max_length=255, default='product', choices=[('top', _('верхнее меню заголовка')), ('bottom', _('нижнее меню'))])
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('на страницу'))

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('меню')
        verbose_name_plural = _('меню')


class File(models.Model):
    orig_file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return os.path.basename(self.orig_file.path)

    class Meta:
        verbose_name = _('Файл')
        verbose_name_plural = _('Файлы')


class Product(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=255)
    name_kk = models.CharField(verbose_name=_('Название Казахский'), max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('Категория'))
    thumbnail = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True, verbose_name=_('Картинка'))
    images = files_widget.ImagesField(null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True, verbose_name=_('содержание'))
    content_kk = RichTextUploadingField(blank=True, null=True, verbose_name=_('содержание Казахский'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('цына'))
    featured = models.BooleanField(default=False, verbose_name=_('показаным'))
    new = models.BooleanField(default=False, verbose_name=_('новый'))

    @display(description=_('просмотр'))
    def my_image_thumbnail(self):
        return get_template('thumbnail_template.html').render({
            'field_name': 'thumbnail',
            'src'       : self.thumbnail.url if self.thumbnail else None,
        })

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')

    def __str__(self):
        if self.name:
            return self.name
        return str(self)
