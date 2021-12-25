from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import render

from apps.business.models import Product, Category


def index(request):
    main_slider_products = Product.objects.filter(featured=True).all()[:5]
    products = Product.objects.all()[:8]
    categories = Category.objects.annotate(count_product=Count('product')).order_by('-count_product').all()[:3]

    context = {
        'categories'          : categories,
        'main_slider_products': main_slider_products,
        'products'            : products
    }

    return render(request, 'business/index.html', context)


def all_products(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    print(category_id)
    if category_id:
        products = products.filter(category_id=category_id)

    page = request.GET.get('page', 1)

    paginator = Paginator(products, 12)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'page_obj'  : products,
        'total'     : paginator.count
    }
    return render(request, 'business/all_products.html', context)


def product_detail(request, product_id=None):
    product = Product.objects.filter(id=product_id).first()
    products = Product.objects.filter(category=product.category).all()[:4]
    context = {
        'products': products,
        'product' : product
    }
    return render(request, 'business/product_detail.html', context=context)
