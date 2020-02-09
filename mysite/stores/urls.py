
from django.urls import path
from. import views
urlpatterns = [
    path('add/',views.addStore, name='add_store'),
    path('showallstore/',views.shwoStore,name='allsotre'),
    path('showallstorehm/',views.shwoStorehm,name='allsotrehm'),
    path('showallstorepr/',views.shwoStorepr,name='allsotrepr'),
    path('ursote/',views.urStore),
    path('db/',views.dashboard,name='dashboard'),
    path('<int:store_id>/', views.detail, name='detailed_store')

]

