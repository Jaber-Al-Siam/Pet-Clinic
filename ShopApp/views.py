from django.shortcuts import render
from ShopApp.models import BuyOfferTable, AdoptOfferTable

# Create your views here.


def buy_request(request):
    obj = BuyOfferTable.objects.all()
    context = {
        "available_buy_offer": obj
    }

    return render(request, 'shop/buy.html', context)



def adopt_request(request):
    obj = AdoptOfferTable.objects.all()
    context = {
        "available_adopt_offer": obj
    }

    return render(request, 'shop/adopt.html', context)
