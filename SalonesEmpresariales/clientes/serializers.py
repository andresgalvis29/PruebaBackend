from clientes.models import Cliente, Evento
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'telefono','correo','departamento','ciudad','edad',
        'created_at','updated_at']

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['created_at','updated_at','cliente','fecha_evento','cantidad_personas','motivo',
        'observaciones','Estado']
