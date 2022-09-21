from django.contrib import admin
from core.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'data_evento', 'local', 'data_criacao', 'usuario')
    list_filter = ('id', 'titulo', 'descricao', 'data_evento', 'local', 'data_criacao', 'usuario')

admin.site.register(Evento, EventoAdmin)