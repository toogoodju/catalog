# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 00:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('name', models.CharField(default=None, max_length=200, primary_key=True, serialize=False)),
                ('context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Context')),
            ],
        ),
        migrations.RemoveField(
            model_name='version',
            name='context',
        ),
        migrations.AddField(
            model_name='version',
            name='app',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='catalog.App'),
            preserve_default=False,
        ),
    ]