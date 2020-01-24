
from django.urls import path
from. import views
urlpatterns = [
    path('add/',views.addStore),
    path('showall/',views.shwoStore),

]

