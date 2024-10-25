from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    compounds = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='products')


class Publications(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()


class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    ingredients = models.TextField()
    full_description = models.TextField()


