from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, CreateView
from datetime import datetime

from .models import Visita
from .forms import VisitaForm

class DashboardView(ListView):
    model = Visita
    template_name = 'visita/index.html'

class RegistroCreateView(CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visita/registro.html'

class BuscarVisitasView(ListView):
    model = Visita
    template_name = 'visita/index.html'
    context_object_name = 'visitas'
    paginate_by = 20  # Opcional: para paginar los resultados

    def get_queryset(self):
        queryset = super().get_queryset()
        texto = self.request.GET.get('texto', '')
        fecha_inicial = self.request.GET.get('fecha_inicial', '')
        fecha_final = self.request.GET.get('fecha_final', '')

        if texto:
            queryset = queryset.filter(
                Q(visitante__icontains=texto) |
                Q(visitante_doc__icontains=texto) |
                Q(entidad__icontains=texto) |
                Q(funcionario__icontains=texto) |
                Q(funcionario_doc__icontains=texto) |
                Q(area__icontains=texto) |
                Q(sucursal__icontains=texto)
            )

        if fecha_inicial and fecha_final:
            fecha_inicial = datetime.strptime(fecha_inicial, '%d/%m/%Y').date()
            fecha_final = datetime.strptime(fecha_final, '%d/%m/%Y').date()
            queryset = queryset.filter(fecha__range=[fecha_inicial, fecha_final])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texto'] = self.request.GET.get('texto', '')
        context['fecha_inicial'] = self.request.GET.get('fecha_inicial', '')
        context['fecha_final'] = self.request.GET.get('fecha_final', '')
        return context