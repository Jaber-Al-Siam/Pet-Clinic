from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserInfoTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpj', upload_to='user')

    def __str__(self):
        return f'{self.user.username} Profile'
