from django.db import models

class Artist(models.Model):
    name = models.CharField('Nom', max_length=200, unique=True)

    class Meta:
        verbose_name = "Auteur"

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField('Nom', max_length=200)
    email = models.EmailField('Email', max_length=200)

    class Meta:
        verbose_name = "Client"

    def __str__(self):
        return self.name


class Album(models.Model):
    reference = models.IntegerField('Référence', null=True)
    create_at = models.DateTimeField('Date de création', auto_now_add=True)
    available = models.BooleanField('Disponible', default=True)
    title = models.CharField('Titre', max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    class Meta:
        verbose_name = "Album"

    def __str__(self):
        return self.title


class Booking(models.Model):
    create_at = models.DateTimeField('Date de création', auto_now_add=True)
    contacted = models.BooleanField('Contacté', default=False)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Reservation"

    def __str__(self):
        return self.contact.name + "(" + self.album.title + ")"

