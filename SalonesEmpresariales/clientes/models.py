from django.db import models
from djchoices import DjangoChoices, ChoiceItem


# Create your models here.
class Cliente(models.Model):
    id = models.CharField("documento de identidad", primary_key=True, unique=True, max_length=11)
    nombre = models.CharField('nombre del cliente', max_length=32)
    apellido = models.CharField('apellido del cliente', max_length=32)
    telefono = models.CharField('telefono del cliente', max_length=11)
    correo = models.EmailField('correo del cliente', max_length=120)
    departamento = models.CharField('departamento del cliente', max_length=32)
    ciudad = models.CharField('ciudad del cliente', max_length=32)
    edad = models.IntegerField('edad del cliente')
    created_at = models.DateTimeField('creado en', auto_now_add=True, editable=False, blank=True, null=True)
    updated_at = models.DateTimeField('actualizado en', auto_now=True, editable=False, blank=True, null=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return self.nombre


class Evento(models.Model):
    #Clase con la cual vamos a identificar las opciones para la lista desplegable del motivo
    class MotivoChoices(DjangoChoices):
        evento = ChoiceItem('EM', 'Evento Empresarial')
        despedida = ChoiceItem('DE', 'Despedida Empresarial')
        desayuno = ChoiceItem('DEE', 'Desayuno Empresarial')
        almuerzo = ChoiceItem('AL', 'Almuerzo')
    #Clase con la cual vamos a identificar la confirmacion de un evento
    class ConfirmacionChoices(DjangoChoices):
        confirmado=ChoiceItem('confirmado','Evento Confirmado')
        no_confirmado = ChoiceItem('no confirmado','Evento no confirmado')
    #Se muestra cuando fue creado el registro de este evento
    created_at = models.DateTimeField('creado en', auto_now_add=True, editable=False, blank=True, null=True)
    updated_at = models.DateTimeField('actualizado en', auto_now=True, editable=False, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_evento = models.DateField('Fecha de evento')
    cantidad_personas = models.IntegerField('Cantidad de Personas en el evento')
    motivo = models.CharField('Motivo del evento',max_length=32, choices=MotivoChoices.choices)
    observaciones = models.CharField('Observaciones del evento',max_length=32)
    Estado = models.CharField('Estado del evento',max_length=32,choices=ConfirmacionChoices.choices)        

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'
    
    def __str__(self):
        return f'evento del cliente: {Evento.cliente}'
