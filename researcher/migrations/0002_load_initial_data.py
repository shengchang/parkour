# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 09:30
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command

fixture = 'initial_data'


def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='researcher')


def unload_fixture(apps, schema_editor):
    """Brutally delete all entries for this model"""

    Researcher = apps.get_model("researcher", "Researcher")
    Researcher.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
