from django.shortcuts import render
from .models import Program

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def programs(request):
    return render(request, 'main/programs.html')

def contact(request):
    return render(request, 'main/contact.html')

def programs(request):
    programs = Program.objects.all()
    return render(request, 'main/programs.html', {'programs': programs})

