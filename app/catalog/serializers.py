from rest_framework import serializers, fields
from .models import *

class VersionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Version
		fields = ('app','version')


class AppSerializer(serializers.ModelSerializer):
	class Meta:
		model = App
		fields = ('name',)

class PoolSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pool
		fields = ('name', 'nodes')

class HostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Host
		fields = ('name', 'environment')

class ContextSerializer(serializers.ModelSerializer):
	class Meta:
		model = Context
		fields = ('id', 'host', 'path', 'pool', 'app')