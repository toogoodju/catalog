# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20170917_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='app',
            new_name='app_id',
        ),
    ]
