from django.urls import path

from .views import DashboardView, RegistroCreateView

urlpatterns = [
    path("list/", DashboardView.as_view(), name="dashboard"),
    path("register/", RegistroCreateView.as_view(), name="registro"),    
]