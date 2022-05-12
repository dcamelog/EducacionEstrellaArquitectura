from django.urls import path,re_path,include
from . import views

urlpatterns=[
    path('',views.simple_upload,name="index"),
    path('logout/',views.logout,name='logout'),
    ]
