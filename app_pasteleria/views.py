from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404
from .models import Producto

def ver_producto(request, id_producto):
    producto = get_object_or_404(Producto, ID_producto=id_producto)
    return render(request, 'categoria/ver_producto.html', {'producto': producto})

def inicio_pasteleria(request):
    productos = Producto.objects.all().order_by('ID_producto')
    return render(request, 'inicio.html', {'productos': productos})

def agregar_pasteleria(request):
    # muestra formulario para agregar producto
    if request.method == 'GET':
        return render(request, 'categoria/agregar_producto.html')
    # si POST lo manejo en realizar_actualizacion_pasteleria para simplificar
    return redirect('inicio_pasteleria')

def realizar_actualizacion_pasteleria(request):
    # maneja creación de nuevo producto (desde agregar_producto.html)
    if request.method == 'POST':
        nombre = request.POST.get('nombre','')
        categoria = request.POST.get('categoria','')
        descripcion = request.POST.get('descripcion','')
        precio = request.POST.get('precio') or 0
        stock = request.POST.get('stock') or 0
        unidad_medida = request.POST.get('unidad_medida','unidad')

        Producto.objects.create(
            nombre=nombre,
            categoria=categoria,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            unidad_medida=unidad_medida
        )
    return redirect('inicio_pasteleria')

def actualizar_pasteleria(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'categoria/actualizar_producto.html', {'producto': producto})

def borrar_pasteleria(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'categoria/borrar_producto.html', {'producto': producto})

def realizar_borrar_pasteleria(request, pk):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
    return redirect('inicio_pasteleria')

def realizar_actualizar_producto(request, pk):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, pk=pk)
        producto.nombre = request.POST.get('nombre','')
        producto.categoria = request.POST.get('categoria','')
        producto.descripcion = request.POST.get('descripcion','')
        producto.precio = request.POST.get('precio') or 0
        producto.stock = request.POST.get('stock') or 0
        producto.unidad_medida = request.POST.get('unidad_medida','unidad')
        producto.save()
    return redirect('inicio_pasteleria')
