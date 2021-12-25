from urllib.parse import unquote

from django import template
from django.template.defaultfilters import stringfilter
from django.utils import translation
from django.utils.safestring import mark_safe

register = template.Library()


@stringfilter
def unquote_raw(value):
    return unquote(value)


@register.simple_tag
def locale(content_ru, content_kk):
    lang = translation.get_language()
    if lang == 'kk' and content_kk:
        return mark_safe(content_kk)
    return mark_safe(content_ru)
