from django.shortcuts import render
from contactos.models import Contacto

def index(request):

    contactos = Contacto.objects.order_by('nombre')

    context = {
        'contactos': contactos,
    }

    return render(request, 'website/index.html', context)
