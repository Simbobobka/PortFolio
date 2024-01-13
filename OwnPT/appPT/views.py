from django.shortcuts import render
from .models import Files

def home(request):
    portfolio_pdf = Files.objects.all()   
    context = {'portfolio_pdf':portfolio_pdf}    
    return render(request, "index.html", context)

def sertificates(request):
    return render(request, "sertificates.html")

def skills(request):
    return render(request, "skills.html")

def projects(request):
    return render(request, "projects.html")
# Create your views here.
