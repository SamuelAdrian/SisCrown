from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
import json as simplejson
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from gestioncliente.models import Visita, Oportunidad, Seguimiento
from cliente.models import Cliente
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import VisitaForm, OportunidadForm, SeguimientoForm, SeguimientoFormSet
from django.contrib.auth.decorators import login_required
# Las Vistas de la Aplicacion

class BuscarView (TemplateView):
    template_name = 'gestioncliente/buscar.html'

    def post (self, request, *args, **kwargs):
        buscar = request.POST['buscalo']
        clientes_dni = Cliente.objects.filter(dni__contains = buscar)
        if clientes_dni:
            print (clientes_dni)
            print ("Busqueda realizada con su CI")
        else:
            clientes_apellido = Cliente.objects.filter(appaterno__contains = buscar)
            print (clientes_apellido)
            return render (request, 'gestioncliente/buscar.html', {'clientes_apellido':clientes_apellido, 'clientes_apellido':True})



        print (clientes_dni)
        return render (request, 'gestioncliente/buscar.html')

class VisitaList(ListView):
    model = Visita


class VisitaDetail(DetailView):
    model = Visita



class VisitaCreation(CreateView):
    model = Visita
    success_url = reverse_lazy('gestion:visitalist')
    form_class = VisitaForm


class OportunidadList(ListView):
    model = Oportunidad

class OportunidadDetail(DetailView):
    model = Oportunidad

class OportunidadCreation(CreateView):
    model = Oportunidad
    success_url = reverse_lazy('gestion:oportunidadlist')
    form_class = OportunidadForm

class OportunidadUpdate(UpdateView):
    model = Oportunidad
    success_url = '/'
    form_class = OportunidadForm

class OportunidadDelete(DeleteView):
    model = Oportunidad
    success_url = reverse_lazy('oportunidadlist')

class OportunidadSeguimientoCreate(CreateView):
    model = Oportunidad
    form_class = OportunidadForm
    # fields = ['negociacion', 'modelo_interes']
    success_url = reverse_lazy('oportunidadlist')

    def get_context_data(self, **kwargs):
        data = super(OportunidadSeguimientoCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['seguimiento'] = SeguimientoFormSet(self.request.POST)
        else:
            data['seguimiento'] = SeguimientoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        seguimiento = context['seguimiento']
        with transaction.atomic():
            self.object = form.save()

            if seguimiento.is_valid():
                seguimiento.instance = self.object
                seguimiento.save()
        return super(OportunidadSeguimientoCreate, self).form_valid(form)

class OportunidadSeguimientoUpdate(UpdateView):
    model = Oportunidad
    fields = ['negociacion', 'modelo_interes']
    success_url = reverse_lazy('oportunidadlist')

    def get_context_data(self, **kwargs):
        data = super(OportunidadSeguimientoUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['seguimiento'] = SeguimientoFormSet(self.request.POST, instance=self.object)
        else:
            data['seguimiento'] = SeguimientoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        seguimiento = context['seguimiento']
        with transaction.atomic():
            self.object = form.save()

            if seguimiento.is_valid():
                seguimiento.instance = self.object
                seguimiento.save()
        return super(OportunidadSeguimientoUpdate, self).form_valid(form)
