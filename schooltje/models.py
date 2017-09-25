# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Richting(models.Model):
    naam = models.CharField(max_length=100)
    omschrijving = models.CharField(max_length=500)
    def __str__(self):
        return "%s" % (self.naam)

class Leraar(models.Model):
    voornaam = models.CharField(max_length=100)
    naam = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='images')
    email = models.CharField(max_length=300)
    def __str__(self):
        return "%s %s" % (self.voornaam, self.naam)

class Klas(models.Model):
    naam = models.CharField(max_length=100)
    numerieke_code = models.IntegerField()
    richting = models.ForeignKey(Richting, on_delete=models.CASCADE)
    leraar = models.ForeignKey(Leraar, on_delete=models.CASCADE)


class Contact(models.Model):
    email = models.CharField(max_length=200)
    nummer = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)