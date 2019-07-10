from django.urls import path
from .views import RegistroUsuario

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name="registrar")
]