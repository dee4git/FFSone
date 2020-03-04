
from django.urls import path
from. import views
urlpatterns = [
    path('<int:store_id>/',views.addPxS ,name="addplan" ),
    path('showall/',views.showPxS , name='all'),
    path('showallphtl/',views.showphtl, name='phtl'),
    path('showallphtl2/',views.showphtl2, name='phtl2'),
    path('showallphtl21/',views.regular, name='r1'),
    path('showallphtl211/',views.regular1, name='r2'),
    path('showallphtl2111/',views.regular2, name='r3'),
    path('s/<int:plan_id>/', views.detail, name='detailed_plan'),
    path('up/<int:x>', views.update, name="upp"),
    path('del/<int:tab_id>', views.delete, name="delp"),

]

