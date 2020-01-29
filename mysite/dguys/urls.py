
from django.urls import path
from. import views
urlpatterns = [
    path('add/',views.addguy, name='add_guy'),
    path('showall/',views.shwoguy),
    #path('ursote/',views.urguy),
    path('<int:dguy_id>/', views.detail, name='detailed_guy')

]

