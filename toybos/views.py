from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class ProductListView(TemplateView):
    template_name = 'product.html'


class ProductDetailView(TemplateView):
    template_name = 'product-inner.html'


class PublicationListView(TemplateView):
    template_name = 'publications.html'


class PublicationDetailView(TemplateView):
    template_name = 'publications-inner.html'


class RecipesListView(TemplateView):
    template_name = 'recipes.html'


class RecipesDetailView(TemplateView):
    template_name = 'recipes-inner.html'