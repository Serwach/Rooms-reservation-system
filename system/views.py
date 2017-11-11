# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Reservation

# Create your views here.
def index(request):
    all_reservations = Reservation.objects.all()
    html = ''

    for reservation in all_reservations:
        url = '/system/' + str(reservation.pk) + '/'
        html += '<a href="' + url + '">' + str(reservation.pk) + '<a/><br/>'

    return HttpResponse(html)

def reservations(request, reservation_id):
    return HttpResponse("<h2>Szczegoly rezerwacji: " + str(reservation_id) + "</h2>")