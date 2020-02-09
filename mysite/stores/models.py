from django.contrib.auth.models import User
from django.db import models

locatoins = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'),('Badda', 'Badda'),('Uttara', 'Uttara'),('Azampur', 'Azampur'),('Khilkhet', 'Khilkhet'),('Banani', 'Banani'),('Nilkhet', 'Nilkhet'),('Bashabo', 'Bashabo'),('Rampura', 'Rampura'),('Mouchak', 'Mouchak'),('Mugdha', 'Mugdha'),('Wari', 'Wari'),('Shahabagh', 'Shahabagh') ]
cats = [('HomeMade', 'HomeMade'), ('Professional', 'Professional')]


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=200, default="Store")
    phone = models.CharField(max_length=200, default="01719588000")
    description = models.TextField(max_length=200, default="Please something about your shop")
    location = models.CharField(max_length=200, choices=locatoins, default='Farmgate')
    category = models.CharField(max_length=200, choices=cats, default='HomeMade')
    thumbnail = models.ImageField(default='store.gif', upload_to='pics', blank=True)
    owner = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
