from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, CreateView
from datetime import datetime
from django.views.generic import FormView
from django.contrib import messages
from .forms import UploadExcelForm
import pandas as pd
from django.urls import reverse_lazy
from django.db import transaction


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
        print(f"request : {self.request}")
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
            print(f"Fechas: {fecha_inicial} {fecha_final}")
            queryset = queryset.filter(fecha__range=[fecha_inicial, fecha_final])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['texto'] = self.request.GET.get('texto', '')
        context['fecha_inicial'] = self.request.GET.get('fecha_inicial', '')
        context['fecha_final'] = self.request.GET.get('fecha_final', '')
        return context

@transaction.atomic
def process_excel(df):
    for index, row in df.iterrows():
        print(f"Procesando fila {index}")
        try:
            print(f"Datos de la fila: {row.to_dict()}")
            visita = Visita.objects.create(
                visitante=row['Visitante'],
                visitante_doc=row['Documento'],
                entidad=row['Entidad'],
                motivo=row['Motivo'],
                funcionario=row['Funcionario'],
                funcionario_doc=row['FunDoc'],
                area=row['Area'],
                sucursal=row['Sucursal'],
                fecha=row['Fecha'],
                hora_ing=row['HoraIng'],
                hora_salida=row['HoraSal']
            )
            print(f"Visita creada con ID: {visita.id}")
        except Exception as e:
            print(f"Error en la fila {index}: {str(e)}")
            # Si quieres que se detenga en el primer error, descomenta la siguiente línea:
            # raise e

class CargarVisitasView(FormView):
    template_name = 'visita/cargar_visitas.html'
    form_class = UploadExcelForm
    success_url = reverse_lazy('visitas:dashboard')  # Cambia esto a la URL que desees después de cargar los datos

    def form_valid(self, form):
        excel_file = form.cleaned_data['archivo']
        df = pd.read_excel(excel_file)
        
        try:
            process_excel(df)
            print("Proceso completado")
        except Exception as e:
            print(f"Error general: {str(e)}")
        
        return super().form_valid(form)