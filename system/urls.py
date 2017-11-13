from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    # /system/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /system/id
    url(r'^(?P<pk>[0-9]+)/$', views.ReservationView.as_view(), name='reservations'),

    # /system/reservations/add
    url(r'reservations/add/$', views.ReservationCreate.as_view(success_url="/system/"), name='reservation-add'),
]
