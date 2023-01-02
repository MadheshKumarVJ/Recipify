from django.views.generic import DetailView

from ..models.recipe import Recipe


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(RecipeDetailView,
    #          self).get_context_data(*args, **kwargs)
    #     context["recipies"] = Recipe.objects.all()
    #     return context
