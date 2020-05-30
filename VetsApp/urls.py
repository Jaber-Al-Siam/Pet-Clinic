from django.urls import path
from .views import view_vets

urlpatterns = [
    path('vets/', view_vets, name="vets_page"),
]
