from django.conf.urls import url
from contactos import views

urlpatterns = [
    url(r'^buscar_contactos/$', views.buscar_contactos, name = 'buscar_contactos'),
    url(r'^modificar_contacto/(?P<contacto_id>\d+)/$', views.modificar_contacto, name = 'modificar_contacto'),
    url(r'^eliminar_contacto/(?P<contacto_id>\d+)/$', views.eliminar_contacto, name = 'eliminar_contacto'),
    url(r'^nuevo_contacto/$', views.nuevo_contacto, name = 'nuevo_contacto'),
]