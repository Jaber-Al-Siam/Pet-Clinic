from django.db import models


# Create your models here.

class BuyOfferTable(models.Model):
    Name = models.CharField(max_length=20, default='SOME STRING')
    Type = models.CharField(max_length=25)
    Description = models.CharField(max_length=100)
    Age = models.IntegerField()
    Color = models.CharField(max_length=30)
    Price = models.IntegerField()
    Image = models.ImageField(default='default.jpj', upload_to='user')

    def __str__(self):
        return self.Name


class AdoptOfferTable(models.Model):
    Name = models.CharField(max_length=20, default='SOME STRING')
    Type = models.CharField(max_length=25)
    Description = models.CharField(max_length=100)
    Age = models.IntegerField()
    Color = models.CharField(max_length=30)
    Image = models.ImageField(default='default.jpj', upload_to='user')

    def __str__(self):
        return self.Name
