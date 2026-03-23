from django.contrib import admin
from .models import *

# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    list_display=("name","nr_registro",)
    ordering=("name",)
    search_fields=("name",)

admin.site.register(PersonalTrainer, PersonalAdmin)

class MembroAdmin(admin.ModelAdmin):
    list_display=("name","nr_registro",)
    ordering=("name",)
    search_fields=("name",)

admin.site.register(Membro, MembroAdmin)

class SessaoAdmin(admin.ModelAdmin):
    list_display=("data_hora")
    ordering=("data_hora",)
    search_fields=("data_hora",)

admin.site.register(Sessao,SessaoAdmin)