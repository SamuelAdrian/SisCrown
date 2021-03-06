from django.contrib import admin
from .models import Perfil, Agencia
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.
@admin.register (Perfil)
class AdminProduct (admin.ModelAdmin):
    list_display = ('usuario','referencia','nacimiento')
    list_filter = ('referencia','nacimiento')
@admin.register (Agencia)
class AdminProduct (admin.ModelAdmin):
    list_display = ('codigo','nombre')
    list_filter = ('codigo','nombre')
