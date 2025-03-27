from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    choices=[
        ('buyer','BUYER'),
        ('seller','SELLER')
    ]
    category=models.CharField(choices=choices, max_length=10, default='buyer')

    def __str__(self):
        return self.username
    