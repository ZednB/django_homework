from django.shortcuts import render
from catalog.models import Product


def home(request):
    context = {
        'product_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя - {name}, телефон - {phone}, сообщение - {message}')
    return render(request, 'catalog/contacts.html')


def base(request, pk):
    context = {
        'product': Product.objects.get(pk=pk),
    }
    return render(request, 'catalog/base.html', context)
