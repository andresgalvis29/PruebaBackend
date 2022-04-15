from django.urls import path
from .views import APIcliente,APIevento,APIclientedetallado,APIeventodetallado,evento_fecha

urlpatterns = [
    path('clientes/',APIcliente),
    path('clientes/<int:pk>/', APIclientedetallado),
    path('eventos/',APIevento),
    path('eventos/<int:pk>',APIeventodetallado),
    path('FechaDeEvento/',evento_fecha)
]