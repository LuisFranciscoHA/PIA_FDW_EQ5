from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('caracteristicas/', views.caracteristicas, name='caracteristicas'),
    path('ventajas/', views.ventajas_view, name='ventajas'),
    path('desventajas/', views.desventajas, name='desventajas'),
    path('apoyo/', views.apoyo, name='apoyo'),
    path('contacto/', views.contacto, name='contacto'),
    path('java/', views.java, name='javascript_leng'),
]
