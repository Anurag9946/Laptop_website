from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def all_prod_cat(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'category': c_page, 'products': products})


def proDetail(request, c_slug, product_slug):
    try:
        product = get_object_or_404(Product, category__slug=c_slug, slug=product_slug, available=True)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})


def payment(request):
    return render(request, 'payment.html')





