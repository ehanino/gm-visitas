from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Visita
from .forms import VisitaForm

class DashboardView(ListView):
    model = Visita
    template_name = 'visita/index.html'

class RegistroCreateView(CreateView):
    model = Visita
    form_class = VisitaForm
    template_name = 'visita/registro.html'