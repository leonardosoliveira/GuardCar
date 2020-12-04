from django.contrib import admin
from django.urls import path, include
from .views import HomeView as v
from .views import *

app_name = "home"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    

]
