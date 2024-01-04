from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')
