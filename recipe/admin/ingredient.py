from django.contrib import admin

from ..models.ingredient import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "quantity",
    )
