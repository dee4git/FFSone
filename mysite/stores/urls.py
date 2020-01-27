
from django.urls import path
from. import views
urlpatterns = [
    path('add/',views.addStore),
    path('showall/',views.shwoStore),
    path('<int:store_id>/', views.detail, name='detailed_store')

]

