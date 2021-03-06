from django.contrib import admin
from .models import Visita, Oportunidad
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register (Visita)
class AdminProduct (admin.ModelAdmin):
    list_display = ('id','agencia')
    list_filter = ('agencia','referencia')

@admin.register (Oportunidad)
class AdminProduct (admin.ModelAdmin):
    list_display = ('id','negociacion')
    list_filter = ('id','tipo_venta')
