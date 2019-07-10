from django.urls import path
from .views import home, galeria, formulario, listar_productos, eliminar_producto, modificar_producto

urlpatterns = [
    path('home/', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('listar-productos/', listar_productos, name="listado_productos"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
]
