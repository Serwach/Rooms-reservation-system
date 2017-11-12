# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Reservation
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    all_reservations = Reservation.objects.all()
    return render(request, 'system/index.html', {'all_reservations': all_reservations})

def reservations(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'system/reservations.html', {'reservation': reservation})