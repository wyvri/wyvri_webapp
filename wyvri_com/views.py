from django.shortcuts import render
from .models import Art

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

def gallery(request):
    context={
        'arts':Art.objects.all()
    }

    return render(request, 'gallery.html', context)