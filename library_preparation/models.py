from django.db import models
from sample.models import Sample


class LibraryPreparation(models.Model):
    sample = models.ForeignKey(Sample, verbose_name='Sample')

    starting_amount = models.FloatField(
        'Starting Amount',
        null=True,
        blank=True,
    )

    starting_volume = models.FloatField(
        'Starting Amount',
        null=True,
        blank=True,
    )

    spike_in_description = models.TextField(
        'Spike-in Description',
        null=True,
        blank=True,
    )

    spike_in_volume = models.FloatField(
        'Spike-in Volume',
        null=True,
        blank=True,
    )

    ul_sample = models.FloatField(
        'µl Sample',
        null=True,
        blank=True,
    )

    ul_buffer = models.FloatField(
        'µl Buffer',
        null=True,
        blank=True,
    )

    pcr_cycles = models.IntegerField(
        'PCR Cycles',
        null=True,
        blank=True,
    )

    concentration_library = models.FloatField(
        'Concentration Library',
        null=True,
        blank=True,
    )

    mean_fragment_size = models.IntegerField(
        'Mean Fragment Size',
        null=True,
        blank=True,
    )

    nM = models.FloatField(
        'nM',
        null=True,
        blank=True,
    )

    file = models.FileField(
        upload_to='benchtop_protocols/%Y/%m/%d/',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Library Preparation'
        verbose_name_plural = 'Library Preparation'

    def __str__(self):
        return self.sample.name
