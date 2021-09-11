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

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  template_name = "vetoffice/Recipe_create_form.html"
  form_class = RecipeCreateForm

class IngredientCreate(LoginRequiredMixin, CreateView):
  model=Ingredient
  template_name = "vetoffice/Ingredient_create_form.html"
  form_class = IngredientCreateForm

class PurchaseCreate(LoginRequiredMixin, CreateView):
  model=Purchase
  template_name = "vetoffice/Purchase_create_form.html"
  form_class = PurchaseCreateForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  template_name = "vetoffice/Recipe_update_form.html"
  form_class = RecipeUpdateForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = "vetoffice/Ingredient_update_form.html"
  form_class = IngredientUpdateForm

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
  model = Purchase
  template_name = "vetoffice/Purchase_update_form.html"
  form_class = PurchaseUpdateForm

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  template_name = "vetoffice/Recipe_delete_form.html"
  success_url = "/Recipe/list"

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "vetoffice/Ingredient_delete_form.html"
  success_url = "/Ingredient/list"

class PurchaseDelete(LoginRequiredMixin, DeleteView):
  model = Purchase
  template_name = "vetoffice/Purchase_delete_form.html"
  success_url = "/Purchase/list"