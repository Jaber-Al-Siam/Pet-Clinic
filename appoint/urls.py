
from django.urls import path
from .views import appoint

urlpatterns = [
    path('appoint/', appoint, name = 'appoint')
]