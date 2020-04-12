from django.urls import path
from .views import home, vets

urlpatterns = [
    path('', home, name="Home"),
    path('vets/', vets, name="Vets"),
]
