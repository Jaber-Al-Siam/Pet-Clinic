from django.shortcuts import render
from ShopApp.models import BuyTable, AdoptTable


# Create your views here.


def buy(request):
    '''obj = BuyTable.objects.get(id=1)'''
    context = {
        "data": "obj"
    }

    return render(request, 'shop/buy.html', context)


def adopt(request):
    '''obj = AdoptTable.objects.get(id=1)'''
    context = {
        "data": "obj"
    }

    return render(request, 'shop/adopt.html', context)
