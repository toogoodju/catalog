
from datetime import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.postgres.fields import ArrayField

class Environment(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Host(models.Model):
	environment = models.ForeignKey('Environment', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, primary_key=True)
	notes = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def sorted_context_set(self):
		return self.context_set.order_by('path')

class Context(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)
    pool = models.ForeignKey('Pool', blank=True, null=True)
    app = models.ForeignKey('App', blank=True, null=True)

    def __str__(self):
        return self.path


class Pool(models.Model):
	name = models.CharField(max_length=200, primary_key=True, default=None)
	nodes = ArrayField(models.CharField(max_length=200, blank=True, null=True))
	monitor = models.ForeignKey('Monitor', blank=True, null=True)

	def __str__(self):
		return self.name

class Monitor(models.Model):
	name = models.CharField(max_length=200, primary_key=True, default=None)
	path = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Version(models.Model):
	version = models.CharField(max_length=200)
	created = models.DateTimeField(default=datetime.now, blank=True)
	app = models.ForeignKey('App')


class App(models.Model):
	name = models.CharField(max_length=200, primary_key=True, default=None)

	def sorted_version_set(self):
		return self.version_set.order_by('created')

	def get_latest_version(self, app_name):
		return self.version_set.filter(app=app_name).latest('created')

