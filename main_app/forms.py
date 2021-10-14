from django import forms
from .models import *
from django.forms.widgets import Textarea

class Login_Form(forms.Form):
    email= forms.EmailField(label='Email', max_length=20, min_length=6)
    password= forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)

class Registration_Form(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=20, min_length=2)
    last_name= forms.CharField(label='Last Name' , max_length=20, min_length=2)
    email= forms.EmailField(label='Email', max_length=20, min_length=6)
    password= forms.CharField(label='Password', widget=forms.PasswordInput(), min_length=8)
    confirm_password= forms.CharField(label='Confirm Password', widget=forms.PasswordInput(), min_length=8) 

# class Recipe_Form(forms.Form):
#     ingredients_choices=Ingredient.objects.all()
#     name= forms.CharField(label='Recipe Name', max_length=40, min_length=2)
#     description=forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows':2, 'cols':40}))
#     ingredient_needed=forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=ingredients_choices,
#     )
    
    