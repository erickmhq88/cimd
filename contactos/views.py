from django.shortcuts import render

def buscar_contactos(request):
    context = {

    }

    return render(request, 'contactos/buscar_contactos.html', context)

def administrar_contactos(request):
    context = {

    }

    return render(request, 'contactos/administrar_contactos.html', context)

def nuevo_contacto(request):
    context = {

    }

    return render(request, 'contactos/nuevo_contacto.html', context)
