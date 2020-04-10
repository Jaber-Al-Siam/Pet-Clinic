from django.db import models


# Create your models here.

class Vets(models.Model):
    Name = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=30)
    Address = models.CharField(max_length=200)
    University = models.CharField(max_length=100)
    HighestDegree = models.CharField(max_length=50)
    Image = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name
