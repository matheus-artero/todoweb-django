from django.shortcuts import render
from django.http import HttpResponse
from .models import Lista, Item


def view_home(request):
    lista = Lista.objects.all().first()
    items  = Item.objects.filter(lista=lista)
    return render(request, 'aplicativo/index.html', {'lista': lista, 'items': items})