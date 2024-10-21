from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class ProductList(TemplateView):
    template_name = 'product.html'
