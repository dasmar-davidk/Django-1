from . import views
from django.urls import path

urlpatterns = [path('', views.index,name="main"),
               path("2/",views.main)]