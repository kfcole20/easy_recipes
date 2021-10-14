from django.shortcuts import render, redirect
from .forms import *
from django.utils.text import slugify
from users_app.models import *
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'form':Login_Form()
    }
    return render(request, 'index.html', context)

def register(request):
    context={
        'form':Registration_Form()
    }
    return render(request, 'register.html', context)

def login(request):
    login_form= Login_Form(request.POST)
    errors=User.objects.verify_login(login_form.data)
    if request.method!= 'POST':
        return redirect('/')
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if login_form.is_valid():
        logged_user=User.objects.filter(email=login_form.data['email'])[0]
        request.session['id']=logged_user.id
        return redirect('/home')

def create(request):
    registration_form=Registration_Form(request.POST)
    errors= User.objects.register(registration_form.data)
    if request.method!= 'POST':
        return redirect('/register')
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/register')
    if registration_form.is_valid():
        new_user= User.objects.create(
            first_name= registration_form.data['first_name'],
            last_name=registration_form.data['last_name'],
            email=registration_form.data['email'],
            password= bcrypt.hashpw(registration_form.data['password'].encode(), bcrypt.gensalt()).decode()
        )
        request.session['id']= new_user.id
        return redirect('/home')

def home(request):
    context={
        'user':User.objects.get(id=request.session['id'])
    }
    return render(request, 'main.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add_recipe(request):
    return render(request, 'add_recipe.html')