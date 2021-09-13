from django.db import models
import datetime
# from django.contrib.auth.models import User

class Recipe(models.Model):
    meal = models.CharField(max_length=100)
    cost = models.FloatField(default=0)


    ingredients = models.CharField(max_length=50)

    # def ingredients_cost(self):
    #     cost = 0
        
    #     return cost

    def get_absolute_url(self):
        return '/recipe/list'
    
    def __str__(self):
        return self.meal


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.FloatField(default=0)
    inventory = models.IntegerField(default=0)

    def ingredient_cost(self):
        return self.unit_price * self.inventory

    def get_absolute_url(self):
        return '/ingredient/list'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    menu_item = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ["-date"]

    def day_revenue(self):
        return self.objects.aggregate(models.Sum("date"))

    def today(self):
        return datetime.date.today()

    def get_absolute_url(self):
        return '/purchase/list'
    
    def __str__(self):
        return self.menu_item


# class RecipeIngCost(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#     quantity = models.FloatField(default=0)

#     def ing_cost(self):
#         return self.ingredient * self.quantity