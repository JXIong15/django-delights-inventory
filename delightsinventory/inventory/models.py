from django.db import models
# from django.contrib.auth.models import User

class Recipe(models.Model):
    meal = models.CharField(max_length=100)
    ingredient = models.CharField(max_length=50)
    cost = models.IntegerField(default=0)

    def get_absolute_url(self):
        return '/recipe/list'


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)

    def get_absolute_url(self):
        return '/ingredient/list'


class Purchase(models.Model):
    menu_item = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return '/purchase/list'