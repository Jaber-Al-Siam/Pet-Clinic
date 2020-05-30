from django.db import models

# Create your models here.

class appoint(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    details = models.TextField(max_length=500, blank=True)


