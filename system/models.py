# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + self.subject

    def get_absolute_url(self):
        return reverse('reservations.detail', kwargs={'pk': self.pk})

class Room(models.Model):
    number = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.number + ' ' + self.building

class Reservation(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return format(self.time)