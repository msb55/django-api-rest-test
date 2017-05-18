from django.contrib import admin

from .models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'date']
	search_fields = ['name']

admin.site.register(Evento, EventoAdmin)