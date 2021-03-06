from django.forms import ModelForm
from django import forms
from .models import Agencia, Perfil
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput

class AgenciaForm (forms.ModelForm):
    class Meta:
        model = Agencia

        fields = [
            'codigo',
            'nombre',
            'foto',
            'telefono',
            'descripcion',
            'empresa',
            'pais',
            'ciudad',
            'referencia',
            'lat',
            'lng',
            'observacion',
        ]
        labels = {
            'codigo': 'Codigo de Agencia',
            'nombre': 'Nombre de la Agencia',
            'foto': 'Foto de la Agencia',
            'telefono':'Telefono de Contacto',
            'descripcion': 'Descripcion',
            'empresa':'Empresa',
            'pais':'Pais',
            'ciudad':'Ciudad',
            'referencia':'Direccion',
            'lat':'Latitud',
            'lng':'Longitud',
            'observacion':'Observacion',
        }
        widgets = {
            'codigo': forms.TextInput (attrs={'class':'form-control'}),
            'nombre': forms.TextInput (attrs={'class':'form-control'}),
            'foto':  forms.ClearableFileInput(),
            'telefono': forms.TextInput (attrs={'class':'form-control'}),
            'descripcion': forms.Textarea (attrs={'class':'form-control'}),
            'empresa': forms.Select (attrs={'class':'form-control'}),
            'pais': forms.Select (attrs={'class':'form-control'}),
            'ciudad': forms.Select (attrs={'class':'form-control'}),
            'referencia': forms.TextInput (attrs={'class':'form-control'}),
            'lat': forms.TextInput (attrs={'class':'form-control'}),
            'lng': forms.TextInput (attrs={'class':'form-control'}),
            'observacion': forms.Textarea (attrs={'class':'form-control'}),
        }


class RegistroForm (UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo Electronico',
        }
        widgets = {
            'username': forms.TextInput (attrs={'class':'form-control'}),
            'first_name': forms.TextInput (attrs={'class':'form-control'}),
            'last_name': forms.TextInput (attrs={'class':'form-control'}),
            'email': forms.TextInput (attrs={'class':'form-control'}),
        }

class PerfilForm (forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'ci',
            'usuario',
            'referencia',
            'lat',
            'lng',
            'genero',
            'nacimiento',
            'cel_corp',
            'celular',
            'telefono',
            'interno',
            'cargo',
            'area',
            'foto',
            'agencia',
            'estado',
        ]
        labels = {
            'ci':'Cedula de Identidad',
            'usuario':'Usuario',
            'referencia':'Direccion',
            'lat':'Latitud',
            'lng':'Longitud',
            'genero':'Genero',
            'nacimiento':'Fecha de Nacimiento',
            'cel_corp':'Celular Corporativo',
            'celular':'Celular Personal',
            'telefono':'Telefono Fijo Personal',
            'interno':'Interno',
            'cargo':'Cargo',
            'area':'Area',
            'foto':'Foto de Perfil',
            'agencia':'Agencia',
            'estado':'Estado',
        }
        widgets = {
            'ci':forms.TextInput (attrs={'class':'form-control'}),
            'usuario':forms.Select (attrs={'class':'form-control'}),
            'referencia':forms.TextInput (attrs={'class':'form-control'}),
            'lat':forms.TextInput (attrs={'class':'form-control'}),
            'lng':forms.TextInput (attrs={'class':'form-control'}),
            'genero':forms.RadioSelect (attrs={'class':'radio-custom radio-inline'}),
            'nacimiento': forms.DateInput(attrs={'class':'form-control'}),
            'cel_corp':forms.TextInput (attrs={'class':'form-control'}),
            'celular':forms.TextInput (attrs={'class':'form-control'}),
            'telefono':forms.TextInput (attrs={'class':'form-control'}),
            'interno':forms.TextInput (attrs={'class':'form-control'}),
            'cargo':forms.Select (attrs={'class':'form-control'}),
            'area':forms.Select (attrs={'class':'form-control'}),
            'foto':forms.ClearableFileInput(),
            'agencia':forms.Select (attrs={'class':'form-control'}),
            'estado':forms.Select (attrs={'class':'form-control'}),
        }




#mydate = forms.DateField(widget=widgets.AdminDateWidget)

# widgets
#
# TextInput
# Textarea
#SelectDateWidget
#CheckboxSelectMultiple
#RadioSelect
