from django.db import models


# Create your models here.

class BuyTable(models.Model):
    Name = models.CharField(max_length=20, default='SOME STRING')
    Type = models.CharField(max_length=25)
    Description = models.CharField(max_length=100)
    Age = models.IntegerField()
    Color = models.CharField(max_length=30)
    Price = models.IntegerField()
    Image = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name


class AdoptTable(models.Model):
    Name = models.CharField(max_length=20, default='SOME STRING')
    Type = models.CharField(max_length=25)
    Description = models.CharField(max_length=100)
    Age = models.IntegerField()
    Color = models.CharField(max_length=30)
    Image = models.CharField(max_length=1000)

    def __str__(self):
        return self.Name
