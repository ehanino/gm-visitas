from django.urls import path

from .views import DashboardView, RegistroCreateView, BuscarVisitasView, CargarVisitasView

urlpatterns = [
    path("lista/", DashboardView.as_view(), name="dashboard"),
    path("registro/", RegistroCreateView.as_view(), name="registro"),
    path('buscar/', BuscarVisitasView.as_view(), name='buscar_visitas'),
    path('cargar-visitas/', CargarVisitasView.as_view(), name='cargar_visitas'),
]