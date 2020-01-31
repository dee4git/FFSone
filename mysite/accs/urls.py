from django.contrib import admin
from django.urls import path, include
from. import views
from django.conf import settings
app_name='accs'
urlpatterns=[
    path('reg/',views.signupV , name="signup"),
    path('login/', views.loginV, name='login'),
    path('logout/', views.logoutV , name='logout'),
]