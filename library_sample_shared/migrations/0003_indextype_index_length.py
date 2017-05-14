# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_sample_shared', '0002_load_shared_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='indextype',
            name='index_length',
            field=models.CharField(choices=[('6', '6'), ('8', '8')], default='8', max_length=1, verbose_name='Index Length'),
        ),
    ]
