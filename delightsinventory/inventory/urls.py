from django.urls import path, include
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("account/", include("django.contrib.auth.urls")),
	# Add a path to your signup request below:
  path("signup/", views.SignUp.as_view(), name="signup"),
	# Add a path to your logout request below:
  path("logout/", views.logout_request, name="logout"),
  path("recipe/list", views.RecipeList.as_view(), name="recipelist"),
  path("recipe/create", views.RecipeCreate.as_view(), name="recipecreate"),
  path("recipe/update/<pk>", views.RecipeUpdate.as_view(), name="recipeupdate"),
  path("recipe/delete/<pk>", views.RecipeDelete.as_view(), name="recipedelete"),
  path("ingredient/list", views.IngredientList.as_view(), name="ingredientlist"),
  path("ingredient/create", views.IngredientCreate.as_view(), name="ingredientcreate"),
  path("ingredient/update/<pk>", views.IngredientUpdate.as_view(), name="ingredientupdate"),
  path("ingredient/delete/<pk>", views.IngredientDelete.as_view(), name="ingredientdelete"),
  path("purchase/list", views.PurchaseList.as_view(), name="purchaselist"),
  path("purchase/create", views.PurchaseCreate.as_view(), name="purchasecreate"),
  path("purchase/update/<pk>", views.PurchaseUpdate.as_view(), name="purchaseupdate"),
  path("purchase/delete/<pk>", views.PurchaseDelete.as_view(), name="purchasedelete"),
  path("purchase/date", views.PurchaseList.as_view(), name="purchasedate")
]