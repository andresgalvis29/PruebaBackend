from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cliente,Evento
from .serializers import ClienteSerializer,EventoSerializer
from django.shortcuts import get_object_or_404,render
from .forms import FormularioFechas

# Create your views here.


#Api Rest del cliente para GET  y POST 
@api_view(['GET','POST'])
def APIcliente(request):

    if request.method == 'GET':
        listado_cliente = Cliente.objects.all()
        Serializador_cliente = ClienteSerializer(listado_cliente,many=True)
        return Response(Serializador_cliente.data)

    elif request.method == 'POST':
        Serializador_cliente = ClienteSerializer(data = request.data)
        if Serializador_cliente.is_valid():
            Serializador_cliente.save()
            return Response(Serializador_cliente.data)
        return Response(Serializador_cliente.errors)

#Api rest del cliente para PATCH y DELETE
@api_view(['GET','PATCH','DELETE'])
def APIclientedetallado(request, pk:str):
    if request.method == 'GET':
        listado_cliente = Cliente.objects.get(id=pk)
        serializador_cliente =  ClienteSerializer(listado_cliente)
        return Response(serializador_cliente.data)

    elif request.method == 'PATCH':
        listado_cliente = Cliente.objects.get(id=pk)
        serializador_cliente = ClienteSerializer(listado_cliente,data = request.data,partial=True)
        if serializador_cliente.is_valid():
            serializador_cliente.save()
            return Response(serializador_cliente.data)
        return Response(serializador_cliente.errors)

    elif request.method == 'DELETE':
        listado_cliente = Cliente.objects.get(id=pk)
        listado_cliente.delete()
        return Response('Eliminado')

#Api Rest del evento para GET  y POST 
@api_view(['GET','POST'])
def APIevento(request):

    if request.method == 'GET':
        listado_evento = Evento.objects.all()
        Serializador_evento = EventoSerializer(listado_evento,many=True)
        return Response(Serializador_evento.data)

    elif request.method == 'POST':
        Serializador_evento = EventoSerializer(data = request.data)
        if Serializador_evento.is_valid():
            Serializador_evento.save()
            return Response(Serializador_evento.data)
        return Response(Serializador_evento.errors)

#Api rest del evento para PATCH y DELETE
@api_view(['GET','PATCH','DELETE'])
def APIeventodetallado(request, pk:str):
    if request.method == 'GET':
        try:
            listado_evento = Evento.objects.get(cliente=pk)
        except Evento.DoesNotExist:
            listado_evento = None 
        if listado_evento is not None:
            Serializador_evento =  EventoSerializer(listado_evento)
            return Response(Serializador_evento.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PATCH':
        listado_evento = Evento.objects.get(cliente=pk)
        Serializador_evento = EventoSerializer(listado_evento,data = request.data,partial=True)
        if Serializador_evento.is_valid():
            Serializador_evento.save()
            return Response(Serializador_evento.data)
        return Response(Serializador_evento.errors)

    elif request.method == 'DELETE':
        listado_evento = Evento.objects.get(cliente=pk)
        listado_evento.delete()
        return Response('Eliminado')

#Busqueda de Fechas
@api_view(['GET','POST'])
def evento_fecha(request):
    #if request.method == 'GET':
        #formulario = FormularioFechas()
        #return render(request,'evento/evento.html')
    
    if request.method == 'POST':
        formulario = FormularioFechas(request.POST)
        if formulario.is_valid():
            inf_formulario = formulario.cleaned_data
            fecha_minima = inf_formulario['fecha_inicio']
            fecha_maxima = inf_formulario['fecha_final']
            datos_relacionados_persona = Evento.objects.select_related('cliente').filter(fecha_evento__lte=fecha_maxima,fecha_evento__gte=fecha_minima)
            formulario = FormularioFechas()
    else:
        formulario = FormularioFechas()
        
    return render(request,'evento/evento.html',{'eventos':datos_relacionados_persona,'form':formulario})
    




    