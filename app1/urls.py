from django.urls import path
from app1.views import *
app_name='somthing1'

urlpatterns = [
    path('first/',first,name="first"),
]
