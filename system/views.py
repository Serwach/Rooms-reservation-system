# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from .models import Reservation
from django.shortcuts import render

# Create your views here.
def index(request):
    all_reservations = Reservation.objects.all()
    return render(request, 'system/index.html', {'all_reservations': all_reservations})

def reservations(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        raise Http404("Rezerwacja nie istnieje")
    return render(request, 'system/reservations.html', {'reservation': reservation})