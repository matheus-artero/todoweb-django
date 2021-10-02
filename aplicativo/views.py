from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def view_home(request):
    return render(request, 'aplicativo/index.html')