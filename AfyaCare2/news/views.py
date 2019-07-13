from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Doctors
# Create your views here.
def welcome(request):
    doctors = Doctors.objects.all()
    return render(request,'welcome.html',{"doctors":doctors})


