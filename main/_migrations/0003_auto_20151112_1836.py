# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151112_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='release_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='year',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
