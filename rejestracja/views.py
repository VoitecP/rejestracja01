from django.shortcuts import render
from rejestracja.models import Shedule

# Create your views here.

def base_view(request):
   # shedules=Shedule.objects.all
    shedules=Shedule.objects.all()
    
    return render(request, 'rejestracja/base.html', {'shedules':shedules})