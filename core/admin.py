from django.contrib import admin
from core.models import Consulta

# Register your models here.

class ConsultaAdmin(admin.ModelAdmin):
    list_display =('titulo','data_consulta','data_criacao')
    list_filter = ('usuario',)






admin.site.register(Consulta,ConsultaAdmin)