from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BusinessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.business'
    verbose_name = _('Основной')
