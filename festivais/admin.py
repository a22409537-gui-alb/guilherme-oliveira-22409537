from django.contrib import admin
from .models import *

# Register your models here.
class FestivalAdmin(admin.ModelAdmin):
    list_display=("name","date")
    ordering=("name",)
    search_fields=("name",)

admin.site.register(Festival,FestivalAdmin)

class GeneroAdmin(admin.ModelAdmin):
    list_display=("name",)
    ordering=("name",)
    search_fields=("name",)

admin.site.register(Genero,GeneroAdmin)

class BandaAdmin(admin.ModelAdmin):
    list_display=("name",)
    ordering=("name",)
    search_fields=("name",)

admin.site.register(Banda,BandaAdmin)