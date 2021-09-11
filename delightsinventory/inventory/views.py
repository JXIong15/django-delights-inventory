from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Ingredient, Purchase
from .forms import RecipeCreateForm, RecipeUpdateForm, IngredientCreateForm, IngredientUpdateForm, PurchaseCreateForm, PurchaseUpdateForm

from django.urls import reverse_lazy
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
#   context = {"name": request.user}
# return render(request, "inventory/home.html", context)
  return render(request, "inventory/home.html")

class RecipeList(ListView):
    model = Recipe

class IngredientList(ListView):
    model = Ingredient

class PurchaseList(ListView):
    model = Purchase

class RecipeCreate(CreateView):
  model = Recipe
  template_name = "inventory/recipe_create_form.html"
  form_class = RecipeCreateForm

class IngredientCreate(CreateView):
  model=Ingredient
  template_name = "inventory/ingredient_create_form.html"
  form_class = IngredientCreateForm

class PurchaseCreate(CreateView):
  model=Purchase
  template_name = "inventory/purchase_create_form.html"
  form_class = PurchaseCreateForm

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

class RecipeUpdate(UpdateView):
  model = Recipe
  template_name = "inventory/recipe_update_form.html"
  form_class = RecipeUpdateForm

class IngredientUpdate(UpdateView):
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"
  form_class = IngredientUpdateForm

class PurchaseUpdate(UpdateView):
  model = Purchase
  template_name = "inventory/purchase_update_form.html"
  form_class = PurchaseUpdateForm

class RecipeDelete(DeleteView):
  model = Recipe
  template_name = "inventory/recipe_delete_form.html"
  success_url = "/recipe/list"

class IngredientDelete(DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"
  success_url = "/ingredient/list"

class PurchaseDelete(DeleteView):
  model = Purchase
  template_name = "inventory/purchase_delete_form.html"
  success_url = "/purchase/list"