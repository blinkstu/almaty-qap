from django.conf.urls import url
from django.urls import path

from apps.business import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all_products/<int:category_id>', views.all_products, name='all_products_category'),
    url(r'all_products$', views.all_products, name='all_products'),
    path('product/<int:product_id>', views.product_detail, name='product_detail')
]
