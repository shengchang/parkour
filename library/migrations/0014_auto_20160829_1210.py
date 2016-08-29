# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import functools
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_sample_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('file', models.FileField(upload_to=functools.partial(library.models._update_filename, *(), **{'path': 'libraries/%Y/%m/%d/'}))),
            ],
        ),
        migrations.AddField(
            model_name='library',
            name='files',
            field=models.ManyToManyField(to='library.FileLibrary'),
        ),
    ]
