from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="reviews")

    ratingChoices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, "5")
    ]

    rating = models.IntegerField(choices=ratingChoices, blank=True)

    def __str__(self):
        return self.title