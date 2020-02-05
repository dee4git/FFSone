from django.contrib import admin

# Register your models here.
from .models import Enrolment , Rating
admin.site.register(Enrolment)
admin.site.register(Rating)