from django.db import models

# Create your models here.

class Evento(models.Model):
	name = models.CharField(max_length = 200, verbose_name='Nome')
	description = models.TextField(verbose_name='Descrição')
	date = models.DateTimeField(verbose_name='Data do Evento')
