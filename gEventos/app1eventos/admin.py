from django.contrib import admin
from .models import Evento, Usuario, RegistroEvento 

# Register your models here.
admin.site.register(Evento)
admin.site.register(Usuario)
admin.site.register(RegistroEvento)