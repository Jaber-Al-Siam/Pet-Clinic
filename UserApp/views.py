from django.shortcuts import render
from .models import SignUPTable


# Create your views here.

def signup(request):
    '''obj = SignUPTable.objects.get(id=1)'''

    context = {
        "data": "obj"
    }

    return render(request, 'user/signup.html', context)


def login(request):
    '''obj = SignUPTable.objects.get(id=1)'''

    context = {
        "data": "obj"
    }

    return render(request, 'user/login.html', context)
