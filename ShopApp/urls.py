from django.urls import path
from .views import buy_request, adopt_request

urlpatterns = [
    path('buy/', buy_request, name="buy_page"),
    path('adopt/', adopt_request, name="adopt_page"),
]
