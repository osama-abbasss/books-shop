from django.shortcuts import render
from products.models import Product
from resume.models import Section


def home_view(request):

    best_sales = Product.objects.filter(lable="best_saler")
    all_prodoucts = Product.objects.all()
    sections = Section.objects.all()
    new_prodoucts = Product.objects.all()[:4]

    template_name = 'home/index.html'
    context = {
    'best_sales':best_sales,
    'sections':sections,
    'all_prodoucts':all_prodoucts,
    'new_prodoucts':new_prodoucts
    }

    return render(request, template_name, context)
