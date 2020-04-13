from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class SignUPTable(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=30)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Image = models.CharField(max_length=1000)


def __str__(self):
    return self.FirstName


class ProfileTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpj', upload_to='user')

    def __str__(self):
        return self.user.username
