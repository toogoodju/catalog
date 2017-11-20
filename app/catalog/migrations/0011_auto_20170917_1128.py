# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20170917_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='context',
            name='app_name',
        ),
        migrations.AddField(
            model_name='context',
            name='app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.App'),
        ),
    ]