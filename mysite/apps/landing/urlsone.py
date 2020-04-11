from django.urls import path
from . import viewsone

urlpatterns = [

path('', viewsone.one, name='one'),

]