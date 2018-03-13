from django.db import models
from support.globals import alert_danger, alert_success

class Contacto(models.Model):
    nombre = models.CharField('Nombre', max_length = 32, blank = False, null = False, unique = False)
    apellidos = models.CharField('Apellidos', max_length = 32, blank = False, null = False, unique = False)
    telefono = models.IntegerField('Telefono', blank = True, null = True, unique = False)
    calle = models.CharField('Calle', max_length = 32, blank = True, null = True, unique = False)
    poblacion = models.CharField('Poblacion', max_length = 16, blank = True, null = True, unique = False)
    codigo_postal = models.CharField('Codigo Postal', max_length = 8, blank = True, null = True, unique = False)
    pais = models.CharField('Pais', max_length = 32, blank = False, null = False, unique = False)
    email = models.EmailField('E-Mail', max_length = 32, blank = False, null = False, unique = True)
    sitio_web = models.URLField('Sitio Web', max_length = 32, blank = True, null = True, unique = False)

    @classmethod
    # Crea un nuevo registro de Contacto en la BD
    def nuevo_contacto(cls, nombre, apellidos, telefono, calle, poblacion, codigo_postal, pais, email, sitio_web):
        # Se comprueba que no exista ningun contacto con el mismo email:
        if cls.objects.filter(email = email):
            message = 'Ya existe un Contacto con email: %s' %(email)
            print(message)
            return {
                'success': False,
                'message': message,
                'class_alert': alert_danger,
                'n_contacto': None,
            }
        else:
            # Si no existe ninguna coincidencia de email, se puede crear el contacto entonces
            n_contacto = cls.objects.create(
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
            message = 'Se ha creado correctamente el Contacto: %s' %(n_contacto)
            print(message)
            return {
                'success': True,
                'message': message,
                'class_alert': alert_success,
                'n_contacto': n_contacto,
            }

    # Modifica un Contacto en particular
    def modificar_contacto(self, nombre, apellidos, telefono, calle, poblacion, codigo_postal, pais, email, sitio_web):
        # Se comprueba que no existe ningun contacto con el email al que se quiere modificar este
        if Contacto.objects.filter(email = email):
            message = 'Ya existe un Contacto con email: %s' % (email)
            print(message)
            return {
                'success': False,
                'message': message,
                'class_alert': alert_danger,
                'm_contacto': None,
            }
        else:
            # Si no existe ninguna coincidencia de email, se puede modificar el contacto entonces
            if self.nombre != nombre:
                self.nombre = nombre
            if self.apellidos != apellidos:
                self.apellidos = apellidos
            if self.telefono != telefono:
                self.telefono = telefono
            if self.calle != calle:
                self.calle = calle
            if self.poblacion != poblacion:
                self.poblacion = poblacion
            if self.codigo_postal != codigo_postal:
                self.codigo_postal = codigo_postal
            if self.pais != pais:
                self.pais = pais
            if self.email != email:
                self.email = email
            if self.sitio_web != sitio_web:
                self.sitio_web = sitio_web
            # Se guardan los cambios que se hayan realizado
            self.save()
            message = 'Se ha modificado correctamente el Contacto: %s' %(self)
            print(message)
            return {
                'success': True,
                'message': message,
                'class_alert': alert_success,
                'm_contacto': self,
            }

    # Elimina un Contacto en particular
    def eliminar_contacto(self):
        self.delete()
        print('Se ha eliminado correctamente el Contacto')

    class Meta:
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return '%s %s (%s)' %(self.nombre, self.apellidos, self.email)

