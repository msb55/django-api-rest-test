
from django.contrib.auth.models import User, Group
from .models import Evento

from rest_framework import serializers

# HyperLinkedModelSerialized semelhante ao ModelSerialized mas utiliza hyperlinks nas relacoes
# url no lugar de id
# url :: HyperLinkedIdentifyField
# mesmo assim pode usar o campo id ('url', 'id', 'username', 'email', 'groups')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'first_name','groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class EventoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Evento
		fields = ('url', 'name', 'description', 'date')