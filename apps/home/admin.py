from django.contrib import admin
from .models import Estacionamentos

@admin.register(Estacionamentos)
class EstacionamentosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco']

# Register your models here.
