from django.shortcuts import render
from django.views.generic import TemplateView

from toybos.models import Category, Product


class HomeView(TemplateView):
    template_name = 'index.html'


class ProductListView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = {
            'products_list': Category.objects.all()
        }
        return context

class ProductDetailView(TemplateView):
    template_name = 'product-inner.html'

    def get_context_data(self, **kwargs):
        context = {
            'Category': Category.objects.get(pk=self.kwargs['pk']),
            'product': Product.objects.get(pk=self.kwargs['pk'])
        }
        return context

class PublicationListView(TemplateView):
    template_name = 'publications.html'


class PublicationDetailView(TemplateView):
    template_name = 'publications-inner.html'


class RecipesListView(TemplateView):
    template_name = 'recipes.html'


class RecipesDetailView(TemplateView):
    template_name = 'recipes-inner.html'