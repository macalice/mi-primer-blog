from django.contrib import admin		#Permite crear el administrador
from .models import Post				#.models es un archivo donde se creó el objeto Post. Está en la misma carpeta que admin.py

admin.site.register(Post)				#Registra nuestro objeto Post en el administrador 
										# de Django para poder consultar o actualizar información



