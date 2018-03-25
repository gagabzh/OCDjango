#! /usr/bin/env python3

# coding: utf-8

from django.test import TestCase
from django.urls import reverse

from .models import Album, Artist, Contact, Booking


# Index page
class IndexPageTestCase(TestCase):
    # test that index page returns a 200
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


# Detail Page
class DetailPageTestCase(TestCase):
    # ran before each test.
    def setUp(self):
        Album.objects.create(title="Transmission Impossible")
        self.album = Album.objects.get(title='Transmission Impossible')

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the items does not exist
    def test_detail_page_returns_404(self):
        album_id = self.album.id + 1
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)


# Booking Page
class BookingPageTestCase(TestCase):

    def setUp(self):
        Contact.objects.create(name="Freddie", email="fred@queen.forever")
        impossible = Album.objects.create(title="Transmission Impossible")
        journey = Artist.objects.create(name="Journey")
        impossible.artists.add(journey)
        self.album = Album.objects.get(title='Transmission Impossible')
        self.contact = Contact.objects.get(name='Freddie')

    # test that a new booking is made
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()  # count bookings before a request
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        response = self.client.post(reverse('store:detail', args=(album_id,)), {
            'name': name,
            'email': email
        })
        new_bookings = Booking.objects.count()  # count bookings after
        self.assertEqual(new_bookings, old_bookings + 1)  # make sure 1 booking was added

    # test that a booking belongs to a contact
    # test that a booking belongs to an album
    # test that an album is not available after a booking is made


class ApiListTestCase(TestCase):
    def setUp(self):
        Album.objects.create(title="Transmission Impossible")
        self.album = Album.objects.get(title='Transmission Impossible')

    def test_api_get_list_album(self):
        response = self.client.get(reverse('store:apiList'))
        self.assertEqual(response.status_code, 200)

    def test_api_post_list_album(self):
        response = self.client.post(reverse('store:apiList'))
        self.assertEqual(response.status_code, 405)

    def test_api_get_show_album(self):
        album_id = self.album.id
        response = self.client.get(reverse('store:apiShow',args=(album_id,)))
        self.assertEqual(response.status_code, 200)

    def test_api_post_show_album(self):
        album_id = self.album.id
        response = self.client.post(reverse('store:apiShow', args=(album_id,)))
        self.assertEqual(response.status_code, 405)
