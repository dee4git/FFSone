from django.db import models
from django.contrib.auth.models import User
locatoins = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'),('Badda', 'Badda'),('Uttara', 'Uttara'),('Azampur', 'Azampur'),('Khilkhet', 'Khilkhet'),('Banani', 'Banani'),('Nilkhet', 'Nilkhet'),('Bashabo', 'Bashabo'),('Rampura', 'Rampura'),('Mouchak', 'Mouchak'),('Mugdha', 'Mugdha'),('Wari', 'Wari'),('Shahabagh', 'Shahabagh') ]

# Create your models here.
class Dguy(models.Model):
    phone=models.CharField(max_length=100, default='0171000000')
    cv=models.FileField(upload_to='cvs',default='cv.doc')
    location = models.CharField(max_length=200, choices=locatoins, default='Farmgate')
    photo = models.ImageField(default='avatar.gif', upload_to='propics', blank=True)
    boy = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
