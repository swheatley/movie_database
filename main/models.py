from django.db import models


import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
# Create your models here.


class DVD(models.Model):
    dvd_title = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    year = models.CharField(null=True, blank=True, max_length=255)
    rating = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.CharField(max_length=255, null=True, blank=True)
    genre = models.ForeignKey('main.Genre', null=True, blank=True)

    def __unicode__(self):
        return self.dvd_title


class MovieCas(Model):
    example_id = columns.Integer(required=False, primary_key=True)
    title = columns.Text(required=False)


class Genre(models.Model):
    genre = models.CharField(max_length=25, null=True, blank=True)

class Studio(models.Model):
    studio = models.CharField(null=True, blank=True, max_length=255)

# #DVD_Title

# Studio


# Status

# Sound

# ID 

# Price

# Rating

# YEAR

# Genere

# DVD_ReleaseDate


