# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='dvd_title',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
