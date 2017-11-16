"""
Przedstawione modele po wykonaniu poleceń 'python manage.py makemigrations system'
oraz 'python manage.py migrate' zostaną odzwierciedlone w bazie danych. Aby dodać
nowy wiersz do tabeli User, należy:
1 - otworzyć terminal, przejść do katalogu projektu
2 - wpisać komende 'python manage.py shell', a następnie:
3 - 'from system.models import User, Room, Reservation
4 - u = User(name="Jan", password="Kowalski", subject="Algebra liniowa")
5 - 'u=save()'
6 - 'exit()'
Program został źle zaplanowany, ponieważ aby stworzyć tabelę użytkowników zgodnie
ze standardem należy ją zaimportować z django.contrib.auth.views. W tym programie
została stworzona zwykła tabela user, spełniająca swoje wymagania.
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

"""
Klasa User przedstawia użytkownika systemu, na pola w bazie danych składają się
pola name, password oraz subject. Metoda __str__ zwraca string, w jaki sposób ma
zostać wypisany User na ekran, natomiast metoda get_absolute_url listę użytkowników
wyświetlaną od końca do początku
"""
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.password + ' ' + self.subject

    def get_absolute_url(self):
        return reverse('reservations.detail', kwargs={'pk': self.pk})


"""
Klasa Room prezentuje sale do zarezerwowania przez użytkownika. Składają się na nią
pola number oraz building. Metoda __str__ analogicznie służy do wypisania sali na ekran
"""

class Room(models.Model):
    number = models.CharField(max_length=100)
    building = models.CharField(max_length=100)

    def __str__(self):
        return self.number + ' ' + self.building

"""
Klasa Reservation prezentuje pojedynczą rezerwację dokonaną przez użytkownika. Zawiera ona
klucze obce tabeli User oraz Room oraz czas rezerwacji.
"""

class Reservation(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    roomid = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return format(self.time)