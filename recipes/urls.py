from django.urls import path

from .views import RecipesListView, RecipesDetailView

urlpatterns = [
    path("<int:pk>", RecipesDetailView.as_view(), name="recipes_detail"),
    path("", RecipesListView.as_view(), name="recipes_list"),
]