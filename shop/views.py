from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug == "search":
        print("##### entering the Search condition #######")
        query = request.GET['search']
        print(query)
        print("update the query to search in sql lit based on the query value and store it in products variable")
        category = get_object_or_404(Category, slug='clutches')
        products = products.filter(category=category)
    elif category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'productlist.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'productdetail.html', {'product': product})
