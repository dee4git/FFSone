
from django.urls import path
from. import views
urlpatterns = [
    path('add/',views.addPxS ,name="addplan" ),
    path('showall/',views.showPxS),
    #path('<int:store_id>/', views.detail, name='detailed_plan')

]

