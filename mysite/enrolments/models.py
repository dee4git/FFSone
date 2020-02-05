from django.db import models
from django.contrib.auth.models import User
from plans.models import Plan
from datetime import datetime, timedelta

# Create your models here.
ch = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0), (5.0, 5.0)]

dr=[(7,7),(14,14),(28,28)]
class Enrolment(models.Model):
    phone=models.CharField(max_length=100, default='01719000000')
    address=models.CharField(max_length=100, default='8/8 Nakahlpra')
    cost=models.FloatField(max_length=100, default=0.00)
    duration = models.IntegerField(max_length=200, choices=dr, default=7)
    startdate=models.DateField(auto_now_add=True)
    plan = models.ForeignKey(Plan, default=None, on_delete=models.CASCADE)
    enroller = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

class Rating(models.Model):
    rating  = models.FloatField(max_length=200, choices=ch, default=5.0)
    enroller = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, default=None, on_delete=models.CASCADE)
    comment= models.TextField(max_length=10000, default="Share your experience with this meal plan , it matters! ❤ ")
