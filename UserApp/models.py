from django.db import models


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
