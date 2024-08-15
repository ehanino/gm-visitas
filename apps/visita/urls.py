from django.urls import path

from .views import DashboardView, RegistroCreateView

urlpatterns = [
    path("lista/", DashboardView.as_view(), name="dashboard"),
    path("registro/", RegistroCreateView.as_view(), name="registro"),    
]