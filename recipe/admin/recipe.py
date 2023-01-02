from django.contrib import admin

from ..models.recipe import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "difficulty_level",
        "created",
        "modified",
        "ingredients",
    )
    list_filter = ("difficulty_level", "created", "author")
    search_fields = ("title", "author", "calories")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "created"
    ordering = ("modified", "created")
