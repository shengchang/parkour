# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-21 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index_generator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poolsize',
            options={'ordering': ['multiplier', 'size']},
        ),
    ]
