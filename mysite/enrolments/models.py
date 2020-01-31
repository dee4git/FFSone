from django.db import models
from django.contrib.auth.models import User
from plans.models import Plan
from datetime import datetime, timedelta

# Create your models here.
dr=[(7,7),(14,14),(28,28)]
class Enrolment(models.Model):
    phone=models.CharField(max_length=100, default='01719000000')
    address=models.CharField(max_length=100, default='8/8 Nakahlpra')
    cost=models.FloatField(max_length=100, default=0.00)
    duration = models.IntegerField(max_length=200, choices=dr, default=7)
    startdate=models.DateField(auto_now_add=True)
    plan = models.ForeignKey(Plan, default=None, on_delete=models.CASCADE)
    enroller = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

