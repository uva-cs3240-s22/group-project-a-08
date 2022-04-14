##Reference: https://www.youtube.com/watch?v=Alua227cOmY

from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Recipe, related_name="saved_recipes", blank=True)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User) #add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User) #add this
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
