from django.conf.urls import url
from . import views

urlpatterns = [
    # /system/
    url(r'^$', views.index, name='index'),

    # /system/id
    url(r'^(?P<reservation_id>[0-9]+)/$', views.reservations, name='reservations'),
]
