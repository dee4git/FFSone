
from django.urls import path
from. import views
urlpatterns= [
    path('p/<int:enl_id>/',views.pay ,name="enl" ),

]

