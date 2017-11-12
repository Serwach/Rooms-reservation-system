# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Reservation, User, Room
from django.contrib import admin

admin.site.register(Reservation)
admin.site.register(User)
admin.site.register(Room)
