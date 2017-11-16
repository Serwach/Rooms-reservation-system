from django.conf.urls import url
from . import views

"""
Plik system/urls.py zawiera linki do urli. Django realizuje architekturę
model-template-view, w tym pliku wywołujemy metody widoków. Mając gotowy
model w bazie danych, aby stworzyć strone należy jeszcze tylko napisać do niej
szablon
"""

app_name = 'system'

urlpatterns = [
    # /system/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /system/id
    url(r'^(?P<pk>[0-9]+)/$', views.ReservationView.as_view(), name='reservations'),

    # /system/reservations/add
    url(r'reservations/add/$', views.ReservationCreate.as_view(success_url="/system/"), name='reservation-add'),

    # /system/login
    url(r'home/$', views.UserCreate.as_view(success_url="/system/"), name='home'),
]
