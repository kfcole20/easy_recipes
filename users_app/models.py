from django.db import models
from django.forms.fields import EmailField
import bcrypt, re
from main_app.forms import *

# Create your models here.
class UserValidation(models.Manager):
    def verify_login(self, post):
        login_form= Login_Form(post)
        errors = {}
        user_logged = User.objects.filter(email=login_form.data['email'])
        if not user_logged:
            errors['no_user'] = 'No user with that email'
            return errors
        if not bcrypt.checkpw(post['password'].encode(), user_logged[0].password.encode()):
            errors['incorrect'] = 'Password/Email combination incorrect'
        return errors
        
    def register(self, post):
        registration_form=Registration_Form(post)
        email_ver= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if registration_form.data['password'] != registration_form.data['confirm_password']:
            errors['password']='Passwords do not match!'
        if not email_ver.match(registration_form.data['email']):
            errors['email']= 'Email format incorrect!'
        return errors




class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserValidation()

    def __str__(self):
        return self.first_name