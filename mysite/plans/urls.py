
from django.urls import path
from. import views
urlpatterns = [
    path('<int:store_id>/',views.addPxS ,name="addplan" ),
    path('showall/',views.showPxS),
    path('s/<int:plan_id>/', views.detail, name='detailed_plan')
    #added s/ just to diffrentiate b2in addplan and detailed_plan

]

