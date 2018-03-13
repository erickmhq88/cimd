from django import forms

class Filtro_Contactos_Form(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length = 32, required = False)
    email = forms.EmailField(label = 'E-Mail', max_length = 32, required = False)
    codigo_postal = forms.CharField(label = 'Codigo Postal', max_length = 8, required = False)
    poblacion = forms.CharField(label = 'Poblacion', max_length = 16, required = False)
    pais = forms.CharField(label = 'Pais', max_length = 16, required = False)

class Contacto_Form(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length = 32, required = True)
    apellidos = forms.CharField(label = 'Apellidos', max_length = 32, required = True)
    telefono = forms.IntegerField(label = 'Telefono', required = False)
    email = forms.EmailField(label = 'E-Mail', max_length = 32, required = True)
    sitio_web = forms.URLField(label = 'Sitio Web', max_length = 32, required = False)
    direccion = forms.CharField(label = 'Direccion', max_length = 64, required = False)
    calle = forms.CharField(label = 'Calle', max_length = 32, required = True)
    poblacion = forms.CharField(label = 'Poblacion', max_length = 16, required = True)
    codigo_postal = forms.CharField(label = 'Codigo Postal', max_length = 8, required = True)
    pais = forms.CharField(label = 'Pais', max_length = 16, required = True)