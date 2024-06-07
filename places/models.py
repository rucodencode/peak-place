from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Place(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
