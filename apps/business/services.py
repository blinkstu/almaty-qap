from django.http import HttpResponse
from django.template import RequestContext, Template

from apps.business.models import Menu
from constance import config


def main_processor(request):
    menus = Menu.objects.order_by('tree_id').filter(level=0).all()
    return {'menus': menus, 'config': config}
