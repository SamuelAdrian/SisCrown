from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.






class Agencia (models.Model):
    codigo = models.CharField(max_length=6,primary_key=True,blank = False,help_text="El codigo de la agencia debe contener 6 digitos Ejemplo: LPZ001",unique = True)
    nombre = models.CharField(max_length=50,blank=False,unique = True)
    foto = models.ImageField ()
    telefono = models.IntegerField(blank = True, null = True)
    descripcion = models.CharField (max_length= 100, blank = True)
    EMPRESAS= (
    ('CROWN','Crown'),
    ('TOYOSA', 'Toyosa'),
    ('TOYOTA', 'Toyota')
    )
    empresa = models.CharField(max_length=30,blank=False, choices= EMPRESAS)
    PAISES= (
    ('BOLIVIA','Bolivia'),
    ('CHILE', 'Chile'),
    ('CUBA', 'Cuba'),
    ('EEUU', 'Estados Unidos')
    )
    pais = models.CharField(max_length=30,blank=False, choices= PAISES)
    CIUDADES= (
    ('LAPAZ','La Paz'),
    ('SANTACRUZ','Santa Cruz'),
    ('COCHABAMBA', 'Cochabamba'),
    ('ORURO', 'Oruro'),
    ('POTOSI', 'Potosi'),
    ('TARIJA', 'Tarija'),
    ('SUCRE', 'Sucre'),
    ('BENI', 'Beni'),
    ('PANDO', 'Pando')
    )
    ciudad = models.CharField(max_length=20,blank=False, choices= CIUDADES)
    referencia = models.CharField (max_length= 150, blank = True)
    lat = models.CharField(max_length = 50,blank = True)
    lng = models.CharField(max_length = 50,blank = True)

    user = models.ForeignKey(User)
    observacion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.nombre



class Perfil(models.Model):
    ci = models.IntegerField(primary_key=True,blank = False,unique = True)
    usuario = models.OneToOneField(User, related_name="profile_user")
    referencia = models.CharField (max_length= 150, blank = True)
    lat = models.CharField(max_length = 50, blank = True)
    lng = models.CharField(max_length = 50, blank = True)
    GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
    )
    genero = models.CharField(max_length=30, choices= GENEROS, default='M')
    nacimiento = models.DateField(default = '1985-01-01')
    cel_corp = models.IntegerField(null=True, blank = True)
    celular = models.IntegerField(null=True,blank = True)
    telefono = models.IntegerField(null=True,blank = True)
    interno = models.IntegerField(null=True,blank = True)
    CARGOS = (
    ('GERENTE', 'Gerente'),
    ('SUBGERENTE', 'Sub Gerente'),
    ('JEFE', 'Jefe'),
    ('RESPONSABLE', 'Responsable'),
    ('ANALISTA', 'Analista'),
    ('EJECUTIVO', 'Ejecutivo'),
    ('ASISTENTE', 'Asistente'),
    ('MECANICO', 'Mecanico'),
    ('MENSAJERO', 'Mensajero'),
    ('PASANTE', 'Pasante')
    )
    cargo = models.CharField(max_length=30, choices= CARGOS)
    AREAS = (
    ('VENTAS', 'Ventas'),
    ('FINANZAS', 'Finanzas'),
    ('CARTERA', 'Cartera'),
    ('MARKETING', 'Marketing'),
    ('CONTABILIDAD', 'Contabilidad'),
    ('RRHH', 'Recursos Humanos'),
    ('SISTEMAS', 'Sistemas'),
    ('SERVICIOS', 'Servicios'),
    ('TALLER', 'Taller'),
    ('LICITACIONES', 'Licitaciones'),
    ('IMPORTACIONES', 'Importaciones'),
    ('LEGAL', 'Legal'),
    ('AGENCIAINTERNA', 'Agencia Interna')
    )
    area = models.CharField(max_length=30, choices= AREAS)
    foto = models.ImageField (blank=False)
    agencia = models.ForeignKey(Agencia, blank=False)
    ESTADOS = (
    ('ACTIVO', 'Activo'),
    ('BAJA', 'Baja'),
    ('BAJATEMP', 'Baja Temporal')
    )
    estado = models.CharField(max_length=15, choices= ESTADOS)

    #datos afps
    AFPS = (
    ('FUTURO', 'Futuro'),
    ('PREVISION', 'Prevision')
    )
    #datos solo para RRHH
    afp = models.CharField(max_length=15, choices= AFPS, blank = True)
    nua = models.CharField(max_length = 20,blank = True)
    numero_afiliacion = models.CharField(max_length = 20,blank = True)

    persona_ref1 = models.CharField(max_length=50,blank=True,unique = False)
    telefono_ref1 = models.IntegerField(null=True,blank = True)

    persona_ref2 = models.CharField(max_length=50,blank=True,unique = False)
    telefono_ref2 = models.IntegerField(null=True,blank = True)

    user = models.ForeignKey(User)
    fecha_creacion = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return str(self.usuario)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Perfil.objects.create(usuario=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.perfil.save()

    # def __str__(self):
    #     return self.nua
