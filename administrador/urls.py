from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base'),
    path('produtos', views.produtos, name="produtos"),
]