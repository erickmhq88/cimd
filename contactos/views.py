from django.shortcuts import render
from contactos.models import Contacto
from contactos.forms import Filtro_Contactos_Form

def buscar_contactos(request):

    # Se determina el total de Contactos existentes que seran mostrados si no se indica ningun criterio de filtrado
    contactos = Contacto.objects.order_by('nombre')

    if request.method == 'POST':
        form = Filtro_Contactos_Form(request.POST)
        if form.is_valid():
            # Se obtiene la informacion de filtrado para limitar los resultados a mostrar
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            codigo_postal = form.cleaned_data['codigo_postal']
            poblacion = form.cleaned_data['poblacion']
            pais = form.cleaned_data['pais']

            # Se van aplicando los filtros segun va siendo necesario
            if nombre:
                contactos = contactos.filter(nombre = nombre)
            if email:
                contactos = contactos.filter(email = email)

            if codigo_postal:
                contactos = contactos.filter(codigo_postal = codigo_postal)

            if poblacion:
                contactos = contactos.filter(poblacion = poblacion)

            if pais:
                contactos = contactos.filter(pais = pais)

            if not contactos:
                message = 'No existen resultados que mostrar'
                class_alert = 'alert alert-info'
            else:
                message, class_alert = None, None

            context = {
                'contactos': contactos,
                'form': form,
                'message': message,
                'class_alert': class_alert,
            }

        else:
            # Si hay errores en el formulario se mantiene con los datos de busqueda cargados y se muestra el mensaje de error al usuario
            context = {
                'contactos': contactos,
                'form': form,
                'message': 'Hay errores en el Formulario',
                'class_alert': 'alert alert-danger',
            }

    else:
        form = Filtro_Contactos_Form()

        context = {
            'contactos': contactos,
            'form': form,
        }

    return render(request, 'contactos/buscar_contactos.html', context)

def administrar_contactos(request):
    context = {

    }

    return render(request, 'contactos/administrar_contactos.html', context)

def nuevo_contacto(request):

    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        telefono = request.POST['telefono']
        email = request.POST['email']
        sitio_web = request.POST['sitio_web']
        calle = request.POST['calle']
        poblacion = request.POST['poblacion']
        codigo_postal = request.POST['codigo_postal']
        pais = request.POST['pais']

        n_contacto = Contacto.nuevo_contacto(
            nombre = nombre,
            apellidos = apellidos,
            telefono = telefono,
            calle = calle,
            poblacion = poblacion,
            codigo_postal = codigo_postal,
            pais = pais,
            email = email,
            sitio_web = sitio_web,
        )

        context = {
            'message': n_contacto['message'],
            'class_alert': n_contacto['class_alert'],
        }

    else:
        context = {}

    return render(request, 'contactos/nuevo_contacto.html', context)
