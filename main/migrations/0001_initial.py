# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dvd_title', models.CharField(max_length=200, null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('year', models.CharField(max_length=255, null=True, blank=True)),
                ('rating', models.CharField(max_length=50, null=True, blank=True)),
                ('release_date', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=25, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studio', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='dvd',
            name='genre',
            field=models.ForeignKey(blank=True, to='main.Genre', null=True),
        ),
    ]
