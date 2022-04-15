from django.contrib import admin
from clientes.models import Cliente, Evento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass
