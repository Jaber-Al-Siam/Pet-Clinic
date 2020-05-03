from django.shortcuts import render
from ServiceApp.models import Service

# Create your views here.


def service_request(request):
    obj = Service.objects.all()
    context = {
        "available_service": obj
    }

    return render(request, 'shop/service.html', context)