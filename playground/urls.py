from django.urls import path 
from . import views  

urlpatterns = [
     path('hello/',views.ask)
     # path('me/',views.hey_me)
]
urlpatterns = [
     path('hello/',views.ask),
     # path('me/',views.hey_me),
     path('temp/',views.temp), # For HTML doc 
]
