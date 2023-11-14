from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Recipe


class RecipesListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"


class RecipesDetailView(DetailView):
    model = Recipe
    template_name = "recipes_detail.html"