from django.shortcuts import render, HttpResponseRedirect
from contactos.models import Contacto
from contactos.forms import Filtro_Contactos_Form, Contacto_Form
from support import globals

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

def nuevo_contacto(request):

    G_APIKey = globals.G_APIKey

    if request.method == 'POST':

        form = Contacto_Form(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            sitio_web = form.cleaned_data['sitio_web']
            calle = form.cleaned_data['calle']
            poblacion = form.cleaned_data['poblacion']
            codigo_postal = form.cleaned_data['codigo_postal']
            pais = form.cleaned_data['pais']

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
                'form': Contacto_Form(),
                'message': n_contacto['message'],
                'class_alert': n_contacto['class_alert'],
                'G_APIPKey': G_APIKey,
            }

        else:
            context = {
                'form': Contacto_Form(request.POST),
                'message': 'Hay errores en el Formulario',
                'class_alert': 'alert alert-danger',
                'G_APIPKey': G_APIKey,
            }

    else:
        context = {
            'form': Contacto_Form(),
            'G_APIPKey': G_APIKey,
        }

    return render(request, 'contactos/nuevo_contacto.html', context)

def modificar_contacto(request, contacto_id):

    contacto = Contacto.objects.get(id = contacto_id)
    G_APIKey = globals.G_APIKey

    datos_contacto = {
        'nombre': contacto.nombre,
        'apellidos': contacto.apellidos,
        'telefono': contacto.telefono,
        'email': contacto.email,
        'sitio_web': contacto.sitio_web,
        'calle': contacto.calle,
        'poblacion': contacto.poblacion,
        'codigo_postal': contacto.codigo_postal,
        'pais': contacto.pais,
    }

    if request.method == 'POST':
        form = Contacto_Form(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellidos = form.cleaned_data['apellidos']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            sitio_web = form.cleaned_data['sitio_web']
            calle = form.cleaned_data['calle']
            poblacion = form.cleaned_data['poblacion']
            codigo_postal = form.cleaned_data['codigo_postal']
            pais = form.cleaned_data['pais']

            m_contacto = contacto.modificar_contacto(
                nombre = nombre,
                apellidos = apellidos,
                telefono = telefono,
                email = email,
                sitio_web = sitio_web,
                calle = calle,
                poblacion = poblacion,
                codigo_postal = codigo_postal,
                pais = pais,
            )

            context = {
                'form': form,
                'message': m_contacto['message'],
                'class_alert': m_contacto['class_alert'],
                'G_APIPKey': G_APIKey,
            }

        else:
            print(form.errors)
            context = {
                'form': form,
                'message': 'Para Modificar la direccion debe escribir en el campo "Direccion" y seleccionar una opcion disponible',
                'class_alert': 'alert alert-danger',
                'G_APIPKey': G_APIKey,
            }

    else:
        context = {
            'form': Contacto_Form(datos_contacto),
            'G_APIPKey': G_APIKey,
        }

    return render(request, 'contactos/modificar_contacto.html', context)

def eliminar_contacto(request, contacto_id):
    contacto = Contacto.objects.get(id = contacto_id)
    contacto.eliminar_contacto()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
