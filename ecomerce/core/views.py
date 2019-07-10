from django.shortcuts import render, redirect
from .models import Marca, Automovil
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def galeria(request):
    return render(request, 'core/galeria.html')


def formulario(request):

    marcas = Marca.objects.all()
    variables = {
        'marcas': marcas
    }

    if request.POST:
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = request.POST.get('txtAnio')
        auto.imagen = request.FILES.get('txtImagen')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca

        try:
            auto.save()
            variables['mensaje'] = 'Guardado correctamente'
        except:
            variables['mensaje'] = 'No se ha podido guardar'

    return render(request, 'core/formulario.html', variables)

# CRUD de automovil


def listar_productos(request):
    autos = Automovil.objects.all()
    return render(request, 'core/listar_productos.html', {
        'autos': autos
    })


def eliminar_producto(request, id):
    # Buscar el automovil que queremos eliminar
    auto = Automovil.objects.get(id=id)

    try:
        auto.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar"
        messages.error(request, mensaje)

    return redirect('listado_productos')

def modificar_producto(request, id):
    #Ubicamos el automovil a moficar
    auto = Automovil.objects.get(id=id)
    marcas = Marca.objects.all() #Solicitamos todas las marcas para llenar el comobox
    variables = {
        'auto':auto,
        'marcas':marcas
    }

    if request.POST:
        auto = Automovil()
        auto.id = request.POST.get('txtid')
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = request.POST.get('txtAnio')
        auto.imagen = request.FILES.get('txtImagen')
        marca = Marca()
        marca.id = request.POST.get('cboMarca')
        auto.marca = marca

        try:
            auto.save()
            messages.success(request, 'Guardado correctamente')
        except:
            messages.error(request, 'No se ha podido modificar')
        return redirect('listado_productos')

    return render(request, 'core/modificar_producto.html', variables)
