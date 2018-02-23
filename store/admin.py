from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Booking, Contact, Album, Artist


class BookingInline(admin.TabularInline):
    model = Booking
    fieldsets = [
        (None, {'fields': ['album', 'contacted']})
        ]  # list columns
    extra = 0
    verbose_name = "Réservation"
    verbose_name_plural = "Réservations"
    readonly_fields = ["create_at", "contacted", "album"]

    def has_add_permission(self, request):
        return False


class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through  # the query goes through an intermediate table.
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline,]  # list of bookings made by a contact


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ['create_at', 'contacted']
    readonly_fields = ["create_at", "contact", 'album_link', 'contacted']

    def album_link(self, booking):
        path = "admin:store_album_change"
        url = reverse(path, args=(booking.album.id,))
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.album.title))

    album_link.short_description = "Album"

    def has_add_permission(self, request):
        return False


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumArtistInline,]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['reference', 'title']