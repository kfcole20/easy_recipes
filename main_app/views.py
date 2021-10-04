from django.shortcuts import render
from .forms import *
from django.utils.text import slugify
from users_app.models import *

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