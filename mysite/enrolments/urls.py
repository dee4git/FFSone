
from django.urls import path
from. import views
urlpatterns = [
    path('<int:plan_id>/',views.addEnrl ,name="enrl" ),
    path('r/<int:plan_id>/', views.rate, name='rate')



]

