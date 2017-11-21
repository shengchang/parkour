# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-17 17:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library_sample_shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NucleicAcidType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('type', models.CharField(choices=[('DNA', 'DNA'), ('RNA', 'RNA')], default='DNA', max_length=3, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Nucleic Acid Type',
                'verbose_name_plural': 'Nucleic Acid Types',
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('status', models.SmallIntegerField(default=0)),
                ('concentration', models.FloatField(verbose_name='Concentration')),
                ('equal_representation_nucleotides', models.BooleanField(default=True, verbose_name='Equal Representation of Nucleotides')),
                ('sequencing_depth', models.PositiveIntegerField(verbose_name='Sequencing Depth')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('is_pooled', models.BooleanField(default=False, verbose_name='Is pooled?')),
                ('barcode', models.CharField(max_length=9, verbose_name='Barcode')),
                ('index_i7', models.CharField(blank=True, max_length=8, null=True, verbose_name='Index I7')),
                ('index_i5', models.CharField(blank=True, max_length=8, null=True, verbose_name='Index I5')),
                ('dilution_factor', models.PositiveIntegerField(blank=True, default=1, verbose_name='Dilution Factor (facility)')),
                ('concentration_facility', models.FloatField(blank=True, null=True, verbose_name='Concentration (facility)')),
                ('sample_volume_facility', models.PositiveIntegerField(blank=True, null=True, verbose_name='Sample Volume (facility)')),
                ('date_facility', models.DateTimeField(blank=True, null=True, verbose_name='Date (facility)')),
                ('amount_facility', models.FloatField(blank=True, null=True, verbose_name='Amount (facility)')),
                ('size_distribution_facility', models.CharField(blank=True, max_length=200, null=True, verbose_name='Size Distribution (facility)')),
                ('comments_facility', models.TextField(blank=True, null=True, verbose_name='Comments (facility)')),
                ('rna_quality', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(11.0)], verbose_name='RNA Quality')),
                ('amplification_cycles', models.PositiveIntegerField(blank=True, null=True, verbose_name='Amplification (cycles)')),
                ('is_converted', models.BooleanField(default=False, verbose_name='Is converted?')),
                ('rna_quality_facility', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(11.0)], verbose_name='RNA Quality (facility)')),
                ('concentration_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sample_shared.ConcentrationMethod', verbose_name='Concentration Method')),
                ('concentration_method_facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='library_sample_shared.ConcentrationMethod', verbose_name='Concentration Method (facility)')),
                ('index_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library_sample_shared.IndexType', verbose_name='Index Type')),
                ('library_protocol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sample_shared.LibraryProtocol', verbose_name='Library Protocol')),
                ('library_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sample_shared.LibraryType', verbose_name='Library Type')),
                ('nucleic_acid_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sample.NucleicAcidType', verbose_name='Nucleic Acid Type')),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sample_shared.Organism', verbose_name='Organism')),
                ('read_length', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sample_shared.ReadLength', verbose_name='Read Length')),
            ],
            options={
                'verbose_name': 'Sample',
                'verbose_name_plural': 'Samples',
            },
        ),
        migrations.RenameField(
            model_name='Sample',
            old_name='date',
            new_name='create_time',
        ),
        migrations.AlterField(
            model_name='sample',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create Time'),
        ),
        migrations.AddField(
            model_name='sample',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Time'),
        ),
    ]
