from django.shortcuts import render
from .models import Art

# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)

def home(request):
    context={
        'arts':Art.objects.all()
    }

    return render(request, 'home.html', context)