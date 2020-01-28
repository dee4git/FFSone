
from django.urls import path
from. import views
urlpatterns = [
    path('add/',views.addStore, name='add_store'),
    path('showall/',views.shwoStore),
    path('ursote/',views.urStore),
    path('<int:store_id>/', views.detail, name='detailed_store')

]

