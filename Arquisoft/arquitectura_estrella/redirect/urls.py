from django.urls import path,re_path,include
from . import views

urlpatterns=[
    path('fail/',views.simple_upload,name="fail"),
    ]
