from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.views import generic
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *
from .mixins import *


class BaseView(generic.TemplateView):
    template_name = 'catalog/base.html'


class EnvironmentView(generic.ListView):
	template_name = 'catalog/environment.html'
	queryset = Host.objects.all()

	def get_context_data(self, **kwargs):
		ctx = super(EnvironmentView, self).get_context_data(**kwargs)
		ctx['hosts'] = Host.objects.filter(environment__name=self.kwargs['env']).order_by('name')
		ctx['apps'] = App.objects.all()
		ctx['versions'] = Version.objects.all()
		return ctx

class VersionView(generic.ListView):
	template_name = 'catalog/versions.html'
	queryset = Version.objects.all()

	def get_context_data(self, **kwargs):
		ctx = super(VersionView, self).get_context_data(**kwargs)
		ctx['versions'] = Version.objects.filter(app__name=self.kwargs['app']).order_by('-created')
		ctx['app_name'] = self.kwargs['app']
		return ctx

class VersionViewSet(viewsets.ModelViewSet):
	queryset = Version.objects.all()
	serializer_class = VersionSerializer

class AppViewSet(viewsets.ModelViewSet):
	queryset = App.objects.all()
	serializer_class = AppSerializer

class PoolViewSet(viewsets.ModelViewSet):
	queryset = Pool.objects.all()
	serializer_class = PoolSerializer
	
	#def create(self, request, *args, **kwargs):
	#	serializer = self.get_serializer(data=request.data)
	#	serializer.is_valid(raise_exception=True)
		#self.perform_create(serializer)
		#headers = self.get_success_headers(serializer.data)
	#	return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class HostViewSet(viewsets.ModelViewSet):
	queryset = Host.objects.all()
	serializer_class = HostSerializer
	lookup_field = 'name'
	lookup_value_regex = '[a-z0-9.]+'

class ContextViewSet(viewsets.ModelViewSet):
	queryset = Context.objects.all()
	serializer_class = ContextSerializer
	#lookup_fields = ('path', 'host')
	#lookup_value_regex = '[a-z0-9./]+'
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('path', 'host')