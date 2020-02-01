from django.db import models
from enrolments.models import  Enrolment
# Create your models here.
class Payment(models.Model):
    enrolment=models.OneToOneField(Enrolment,default=None, on_delete=models.CASCADE )
    refid= models.CharField(max_length=200, default="xxxxxxxx")
