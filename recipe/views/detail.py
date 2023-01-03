from django.views.generic import DetailView

from ..models.recipe import Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/detail.html"
