from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Recipe, Ingredient, Purchase
from .forms import RecipeCreateForm, RecipeUpdateForm, IngredientCreateForm, IngredientUpdateForm, PurchaseCreateForm, PurchaseUpdateForm
from .filters import PurchaseFilter

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

@login_required
def home(request):
    context = {"name": request.user}
    return render(request, "inventory/home.html", context)

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "inventory/recipe_list.html"

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredient_list.html"

class PurchaseList(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchase_list.html"

    def get_context_date(self, **kwargs):
        context = super().get_contect_date(**kwargs)
        context['filter'] = PurchaseFilter(self.request.GET, queryset = self.get_queryset())
        return context

class RecipeCreate(LoginRequiredMixin, CreateView):
  model = Recipe
  template_name = "inventory/recipe_create_form.html"
  form_class = RecipeCreateForm

class IngredientCreate(LoginRequiredMixin, CreateView):
  model=Ingredient
  template_name = "inventory/ingredient_create_form.html"
  form_class = IngredientCreateForm

class PurchaseCreate(LoginRequiredMixin, CreateView):
  model=Purchase
  template_name = "inventory/purchase_create_form.html"
  form_class = PurchaseCreateForm

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

class RecipeUpdate(LoginRequiredMixin, UpdateView):
  model = Recipe
  template_name = "inventory/recipe_update_form.html"
  form_class = RecipeUpdateForm

class IngredientUpdate(LoginRequiredMixin, UpdateView):
  model = Ingredient
  template_name = "inventory/ingredient_update_form.html"
  form_class = IngredientUpdateForm

class PurchaseUpdate(LoginRequiredMixin, UpdateView):
  model = Purchase
  template_name = "inventory/purchase_update_form.html"
  form_class = PurchaseUpdateForm

class RecipeDelete(LoginRequiredMixin, DeleteView):
  model = Recipe
  template_name = "inventory/recipe_delete_form.html"
  success_url = "/recipe/list"

class IngredientDelete(LoginRequiredMixin, DeleteView):
  model = Ingredient
  template_name = "inventory/ingredient_delete_form.html"
  success_url = "/ingredient/list"

class PurchaseDelete(LoginRequiredMixin, DeleteView):
  model = Purchase
  template_name = "inventory/purchase_delete_form.html"
  success_url = "/purchase/list"

def logout_request(request):
  logout(request)
  return redirect("home")