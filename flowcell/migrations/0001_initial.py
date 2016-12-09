# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequencer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('lanes', models.PositiveSmallIntegerField(verbose_name='Number of Lanes')),
                ('lane_capacity', models.PositiveSmallIntegerField(verbose_name='Lane Capacity')),
            ],
        ),
    ]
