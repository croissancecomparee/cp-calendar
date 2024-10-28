from django.db import models

class Type(models.models):
    name=models.CharField(max_length=200)
    description = models.TextField(blank=True)