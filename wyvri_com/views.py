from django.shortcuts import render
from .models import Art
import random

# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)

def home(request):
    context={

    }

    return render(request, 'home.html', context)

def aboutme(request):
    context={

    }

    return render(request, 'aboutme.html', context)

def get_size():
    sizeList = [150, 200, 200, 250, 300]
    return random.choice(sizeList)

def add_size(art):
    art.size = get_size()
    return art

def gallery(request):
    context={
        'arts':map(add_size, Art.objects.all())
    }

    return render(request, 'gallery.html', context)