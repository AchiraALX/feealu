from importlib.resources import contents
from django.db import models

class comments(models.Model):
    content = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True, null=True)
    author = models.CharField(max_length=100, null=True)

# Create your models here.
