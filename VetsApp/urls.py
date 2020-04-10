
from django.urls import path
from .views import home, vets, signup

urlpatterns = [
    path('', home, name="Home"),
    path('vets/', vets, name="Vets"),
    path('signup/', signup, name="SignUP"),
]
