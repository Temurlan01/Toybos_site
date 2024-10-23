from django.contrib import admin
from toybos.models import Recipes, Category, Product, Publications


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('name',)