from django.contrib import admin
from .models import *

# Register your models here.
class TurmaAdmin(admin.ModelAdmin):
    list_display=("nr",)
    ordering = ("nr",)
    search_fields=("nr",)

admin.site.register(Turma, TurmaAdmin)

class AlunoAdmin(admin.ModelAdmin):
    list_display=("nome","nr",)
    ordering = ("nome",)
    search_fields=("nome",)

admin.site.register(Aluno,AlunoAdmin)

class ProfessorAdmin(admin.ModelAdmin):
    list_display=("nome","email",)
    ordering = ("nome",)
    search_fields=("nome",)

admin.site.register(Professor,ProfessorAdmin)