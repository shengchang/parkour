# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 11:05
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'sequencers', app_label='flowcell')


def unload_fixture(apps, schema_editor):
    Sequencer = apps.get_model('flowcell', 'Sequencer')
    Sequencer.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('flowcell', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
