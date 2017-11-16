# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Reservation, User, Room
from django.contrib import admin

"""
W tym pliku następuje dołączenie tabel bazy danych do interfejsu django-admin
pod adresem http://127.0.0.1:8000/admin/
"""
admin.site.register(Reservation)
admin.site.register(User)
admin.site.register(Room)
