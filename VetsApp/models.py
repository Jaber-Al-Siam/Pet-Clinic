from django.db import models


# Create your models here.

class VetsInfoTable(models.Model):
    Name = models.CharField(max_length=100)
    ContactNo = models.CharField(max_length=30)
    Address = models.CharField(max_length=200)
    University = models.CharField(max_length=100)
    HighestDegree = models.CharField(max_length=50)
    Image = models.ImageField(default='default.jpj', upload_to='vets_images')

    def __str__(self):
        return self.Name

