
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorter = request.GET.get('sort', None)
    options = {'name': Phone.objects.all().order_by('name'),
               'max_price': reversed(Phone.objects.all().order_by('price')),
               'min_price': Phone.objects.all().order_by('price'),
               None: Phone.objects.all(),
               }

    context = {'phones': options[sorter]}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
