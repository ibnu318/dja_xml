from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes_detail", args=[str(self.id)])
