from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('flavors/', views.flavors, name='flavors'), 
    path('inventory/', views.inventory, name='inventory'),  
    path('suggestions/', views.suggestions, name='suggestions'), 
]
