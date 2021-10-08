from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields import related
from django.db.models.fields.related import ManyToManyField
from main_app.forms import Recipe_Form
from users_app.models import User

# Create your models here.


class Recipe(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    uploaded_by=models.ForeignKey(User, related_name='recipes', on_delete=CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Ingredient(models.Model):
    name= models.CharField(max_length=255)
    recipe_for= models.ManyToManyField(Recipe, related_name='ingredients_needed')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)