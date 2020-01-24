from django.contrib.auth.models import User
from django.db import models

locatoins = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Wari', 'Wari'), ]
cats = [('HomeMade', 'HomeMade'), ('Professional', 'Professional')]


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=200, default="Store")
    description = models.TextField(max_length=200, default="Please something about your shop")
    location = models.CharField(max_length=200, choices=locatoins, default='Farmgate')
    category = models.CharField(max_length=200, choices=cats, default='HomeMade')
    thumbnail = models.ImageField(default='default.png', upload_to='pics', blank=True)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
