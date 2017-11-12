# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from .models import Reservation

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'system/index.html'
    context_object_name = 'all_reservations'

    def get_queryset(self):
        return Reservation.objects.all()

class ReservationView(generic.DetailView):
    model = Reservation
    template_name = 'system/reservations.html'