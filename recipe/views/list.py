from django.views.generic import ListView

from ..models.recipe import Recipe


class RecipeListView(ListView):
    queryset = Recipe.objects.all()
    paginate_by = 3
    context_object_name = "recipies"
    template_name = "recipe/dashboard.html"
