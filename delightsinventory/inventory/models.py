from django.db import models
# from django.contrib.auth.models import User

class Recipe(models.Model):
    meal = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=50)
    cost = models.FloatField(default=0)

    def get_absolute_url(self):
        return '/recipe/list'
    
    def __str__(self):
        return self.meal


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.FloatField(default=0)
    inventory = models.IntegerField(default=0)

    def get_absolute_url(self):
        return '/ingredient/list'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    menu_item = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return '/purchase/list'
    
    def __str__(self):
        return self.menu_item