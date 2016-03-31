# Nombre: c:\djangogirls\blog\models.py

from django.db import models   	# importar modelos

from django.utils import timezone 	# importar timezone para la fecha correcta


class Post(models.Model):		#Crear un modelo
        author = models.ForeignKey('auth.User')		#Autor de acuerdo una llave foránea.
        title = models.CharField(max_length=200)	#Título con longitud de 200 caracteres
        text = models.TextField()					#Sin longitud de texto especificado
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()	# Asignación de fecha automática al publicarlo
            self.save()								# la información se guarde

        def __str__(self):
            return self.title						# Con un print devuelve el título

    