from django.urls import path
from .views import service_request

urlpatterns = [
    path('service/', service_request, name="service_page"),
]