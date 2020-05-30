from django.shortcuts import render
from .models import VetsInfoTable


# Create your views here.

def home(request):

    context = {
        "name": "Home"
    }

    return render(request, 'index.html', context)


def view_vets(request):
    obj = VetsInfoTable.objects.all()

    context = {
        "vets_data": obj
    }

    return render(request, 'vets/vets.html', context)
