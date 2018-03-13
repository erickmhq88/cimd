from django.conf.urls import url
from contactos import views

urlpatterns = [
    url(r'^buscar_contactos/$', views.buscar_contactos, name = 'buscar_contactos'),
    url(r'^administrar_contactos/$', views.administrar_contactos, name = 'administrar_contactos'),
    url(r'^nuevo_contacto/$', views.nuevo_contacto, name = 'nuevo_contacto'),
]