from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    LEVEL_CHOICES = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    instructions = models.TextField()
    calories = models.PositiveBigIntegerField()
    difficulty_level = models.CharField(
        max_length=10, choices=LEVEL_CHOICES, default="easy"
    )
    preparation_time = models.CharField(max_length=50)

    class Meta:
        app_label = "recipe"

    def __str__(self):
        return self.title
