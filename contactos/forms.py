from django import forms

class Filtro_Contactos_Form(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length = 32, required = False)
    email = forms.EmailField(label = 'E-Mail', max_length = 32, required = False)
    codigo_postal = forms.CharField(label = 'Codigo Postal', max_length = 8, required = False)
    poblacion = forms.CharField(label = 'Poblacion', max_length = 16, required = False)
    pais = forms.CharField(label = 'Pais', max_length = 16, required = False)