from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def appoint(request):
    return  HttpResponse("<h1> This is our appointment</h1>" )