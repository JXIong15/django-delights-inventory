from django import forms
from .models import Recipe, Ingredient, Purchase

# CRUD - Create
class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('meal', 'ingredients', 'cost',)

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'unit_price', 'inventory')

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item', 'date', 'time')

#CRUD - Update
class RecipeUpdateForm(forms.ModelForm):
    #form for updating Recipes
    class Meta:
        model = Recipe
        fields = ('meal', 'ingredients', 'cost',)

class IngredientUpdateForm(forms.ModelForm):
    #form for updating Ingredients
    class Meta:
        model = Ingredient
        fields = ('name', 'unit_price', 'inventory')

class PurchaseUpdateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item', 'date', 'time')