from django.urls import path

from . import views

app_name = 'administrador'

urlpatterns = [
    path('', views.index, name='base'),
    path('produtos', views.produtos, name="produtos"),
]
