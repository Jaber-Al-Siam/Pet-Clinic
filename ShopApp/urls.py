from django.urls import path
from .views import buy, adopt

urlpatterns = [
    path('buy/', buy, name="Buy"),
    path('adopt/', adopt, name="Adopt"),
]
