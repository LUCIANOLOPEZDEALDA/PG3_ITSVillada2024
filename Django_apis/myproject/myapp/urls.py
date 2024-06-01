# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('breweries/', views.brewery_list, name='brewery_list'),
]
