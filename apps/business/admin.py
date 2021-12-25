from django.contrib import admin
from django.contrib.admin import ModelAdmin, display
from django.contrib.auth.admin import UserAdmin
from django.template.loader import get_template
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from apps.business.models import Category, Menu, Product, File, Page


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    model = Category
    search_fields = ['name', 'name_kk']
    list_display = ('tree_actions', 'indented_title')


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    model = Menu
    list_display = ('tree_actions', 'indented_title', 'slug')
    search_fields = ['name']
    list_filter = [
        "slug",
    ]
    fieldsets = (
        (None, {'fields': ('name', 'name_kk', 'slug')}),
        (_('Цели'), {'fields': ('to_page', 'url', 'open_on_new_tab', 'page')}),
    )

    def changelist_view(self, request, extra_context=None):
        if 'slug__exact' not in request.GET:
            q = request.GET.copy()
            q['slug__exact'] = 'top'
            request.GET = q
            request.META['QUERY_STRING'] = request.GET.urlencode()
        return super(MenuAdmin, self).changelist_view(request, extra_context=extra_context)

    class Media:
        js = ('/static/admin/js/hide_attribute.js',)


@admin.register(File)
class FileAdmin(ModelAdmin):
    model = File
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    fieldsets = (
        (_('Оснавной'), {'fields': ('name', 'name_kk', 'category', 'images', 'price', 'featured', 'new')}),
        (_('Содержание'), {'fields': ('content', 'content_kk')}),
    )
    list_filter = ['category', 'featured', 'new']
    model = Product
    autocomplete_fields = ['category']
    list_display = ['name', 'image_tag', 'price', 'category', 'featured', 'new']
    readonly_fields = ('my_image_thumbnail',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:60px;" />'.format(obj.thumbnail.url if obj.thumbnail else None))

    image_tag.short_description = _('Картинка')


@admin.register(Page)
class PageAdmin(ModelAdmin):
    fieldsets = (
        (_('Оснавной'), {'fields': ('title', 'title_kk')}),
        (_('Содержание'), {'fields': ('content', 'content_kk')}),
    )
    model = Page
    list_display = ['title']
