from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    # url(r'^add_alojamiento_completo/(?P<alojamiento_sin_finalizar_id>\d+)/$', views.add_alojamiento_completo, name = 'add_alojamiento_completo'),
]