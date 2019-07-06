from django.shortcuts import render
from .models import *
from . import forms
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request,'HealthKit/Home.html')