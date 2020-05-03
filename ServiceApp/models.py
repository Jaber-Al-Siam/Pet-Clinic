from django.db import models

# Create your models here.


class Service(models.Model):
    Name = models.CharField(max_length=30, default='SOME STRING')
    Description = models.CharField(max_length=200)
    Price = models.IntegerField()

    def __str__(self):
        return self.Name
