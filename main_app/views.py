from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    context={
        'form':Login_Form()
    }
    return render(request, 'index.html', context)