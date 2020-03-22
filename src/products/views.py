from django.shortcuts import render, get_object_or_404
from .models import Product,Image, Category


def products_view(request):
    if request.method == 'POST':
        cat = request.POST.get('cat')
        if cat  != 'all':
            try:
                products = Product.objects.filter(category__category=cat)
            except:
                products = Product.objects.all()
        else:
            products = Product.objects.all()
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    template_name = 'products/books_list.html'
    context = { 'books': products,
                'categories':categories
                }

    return render(request, template_name, context)



def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    template_name = 'products/single-product.html'
    context = { 'book': product,
                'categories':categories
                }

    return render(request, template_name, context)
