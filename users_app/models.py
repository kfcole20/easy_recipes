from django.db import models
from django.forms.fields import EmailField

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email=models.EmailField(max_length=50)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    slug= models.SlugField(unique=True)

    def __str__(self):
        return self.first_name