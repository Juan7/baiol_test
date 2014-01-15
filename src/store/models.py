from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Store(models.Model):
    category_choices = (
        (1, 'toys'),
        (2, 'sports'),
        (3, 'clothes'),
        (4, 'food'),
    )
    
    name = models.CharField(max_length=255)
    category = models.IntegerField(choices=category_choices, default=1)
    owner = models.ForeignKey(User)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
