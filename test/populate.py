#! /usr/bin/env python3

# coding: utf-8

from store.models import Artist, Album


francis = Artist.objects.create(name="Francis Cabrel")
patrick = Artist.objects.create(name="Patrick Bruel")
benabar = Artist.objects.create(name="Benabar")
oldelaf = Artist.objects.create(name="Oldelaf")

album = Album.objects.create(title="Sarbacane")
album.artists.add(francis)

album = Album.objects.create(title="Place des grands hommes")
album.artists.add(patrick)

album = Album.objects.create(title="Les epices du souk du caire")
album.artists.add(benabar)

album = Album.objects.create(title="Les risques du metiers")
album.artists.add(benabar)

album = Album.objects.create(title="Dimanche")
album.artists.add(oldelaf)

album = Album.objects.create(title="Le monde est beau")
album.artists.add(oldelaf)

album = Album.objects.create(title="Le soldat rose")
album.artists.add(francis)
album.artists.add(benabar)

album = Album.objects.create(title="Le bal des enfoirées")
album.artists.add(francis)
album.artists.add(patrick)
album.artists.add(francis)

print("population créée")
