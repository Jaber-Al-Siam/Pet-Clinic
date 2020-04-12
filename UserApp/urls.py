from django.urls import path
from .views import signup, login

urlpatterns = [
    path('signup/', signup, name="SignUP"),
    path('login/', login, name="Login"),
]
