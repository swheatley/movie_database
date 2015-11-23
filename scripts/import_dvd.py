#!/usr/bin/env python

import csv
import sys
import os
from unidecode import unidecode
import string

sys.path.append('..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import DVD, Genre, Studio

import django
django.setup()

print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "dvd.csv"

dvd_csv = os.path.join(dir_name, file_name)
csv_file = open(dvd_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    print row['DVD_Title']

    if row['DVD_Title'][0] not in list(string.punctuation):
        new_genre, created = Genre.objects.get_or_create(genre=row['Genre'])
     

        new_dvd, created = DVD.objects.get_or_create(dvd_title=unidecode(row['DVD_Title']))
        new_dvd.price = row['Price']
        new_dvd.year = row['Year']
        new_dvd.rating = row['Rating']
        new_dvd.release_date = row['Released']

        new_dvd.genre = new_genre
        
        # cluster = Cluster(['127.0.0.1'])
        # session = cluster.connect()
        # session.set_keyspace('movie_database')
        # movie = MovieCas(title=dvd_name)
        # movie.save()
        # cluster.shutdown()

        # movie = MovieCas(title=unidecode(row['DVD_Title']))
        # movie.id = new_dvd.id

        try:
            new_dvd.save()
        except Exception, e:
            print e
            print "lol, no.."


