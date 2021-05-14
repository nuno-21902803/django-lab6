from django.shortcuts import render
from datetime import datetime


def home_page_view(request):
    context = datetime.now()
    ano = datetime.now().year

    return render(request, 'website/home.html',
                  {'hora': context,
                   'year': ano})


def details_page_view(request):
    lista = ['Django', 'HTML', 'Python']
    return render(request, 'website/details.html', {'list': lista})


def about_page_view(request):
    name = "João Lampião"
    return render(request, 'website/about.html', {'nome': name})
