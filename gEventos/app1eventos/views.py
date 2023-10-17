from django.shortcuts import render, redirect
from django.db import connection
from django.db.models import Count
from .models import Evento, RegistroEvento, Usuario
from django.http import HttpResponse

# Create your views here.



def index(request):
    return render(request, 'index.html')    

def formulario_registro(request):
    return render(request, 'formulario_registro.html')

def guardar_usuario(request):
    nombre1 = request.POST['nombre']
    apellido1 = request.POST['apellido']
    #ME QUEDO A
    email1 = request.POST['email']
    contraseña1 = request.POST['contraseña']
    dni1 = request.POST['dni']
    nuevo_registro = Usuario(
        nombre=nombre1,
        apellido=apellido1, 
        email=email1, 
        contraseña=contraseña1, 
        dni=dni1,
        clase='clien')
    nuevo_registro.save()
    return redirect('index')

def validacion(request):
    email1 = request.POST['email']
    contraseña1 = request.POST['contraseña']
    result = Usuario.objects.filter(email=email1, contraseña=contraseña1).first()
    
    if (result):
        if(result.clase=='admin'):
            return redirect('homepage_admin')
        elif(result.clase=='clien'):
            return redirect('homepage_clien')
    else:
        return HttpResponse(f"{email1} and {contraseña1} son incorrectos") 

#ADMIN
def homepage_admin(request):
    eventos = Evento.objects.all()
    context = {'eventos':eventos}
    # context = {'eventos':eventos, 'cantidad_asist': lista}

    return render(request, 'homepage_admin.html', context )

def formulario_nuevo_evento(request):
    return  render(request, 'formulario_nuevo_evento.html')

def crear_evento(request):
    nombre1 = request.POST['nombre']
    lugar1 = request.POST['lugar']
    fechainicio1 = request.POST['fechainicio']
    fechafin1 = request.POST['fechafin']
    Evento.objects.create(
        nombre=nombre1,
        lugar=lugar1,
        fechainicio=fechainicio1,
        fechafin=fechafin1
    )

    return redirect('homepage_admin')

def formulario_modificar_evento(request):
    nombre1 = request.POST['nombre'] 
    evento = Evento.objects.filter(nombre=nombre1).first()
    context = {'evento':evento}

    return  render(request, 'formulario_modificar_evento.html', context)

def modificar_evento(request):
    realname1 = request.POST['real_name']
    nombre1 = request.POST['nombre']
    lugar1 = request.POST['lugar']
    fechainicio1 = request.POST['fechainicio']
    fechafin1 = request.POST['fechafin']

    result = Evento.objects.filter(nombre=realname1).first()
    result.nombre = nombre1
    result.lugar = lugar1
    result.fechainicio = fechainicio1
    result.fechafin = fechafin1
    result.save()
    #QUEDO CON EL PROBLEMA DEL DATETIME-LOCAL
    return redirect('homepage_admin')

def borrar_evento(request):
    nombre1 = request.POST['nombre']
    Evento.objects.filter(nombre=nombre1).delete()    
    return redirect('homepage_admin')


#CLIENTE
def homepage_clien(request):
    eventos = Evento.objects.all()
    asistencias = RegistroEvento.objects.all()
    context = {'eventos':eventos, 'asistencias':asistencias}
    return render(request, 'homepage_clien.html', context)


def formulario_evento_asistir(request):
    event_name=request.POST['nombre']
    context = {'event_name':event_name}
    return render(request, 'formulario_evento_asistir.html', context)

def guardar_asistencia(request):
    email1 = request.POST['email']
    event_name = request.POST['event_name']
    

    try:
        evento1 = Evento.objects.filter(nombre=event_name).first()
        usuario1 = Usuario.objects.filter(email=email1).first()
        RegistroEvento.objects.create(
            evento=evento1,
            usuario=usuario1,
        )
        return redirect('homepage_clien')
    except:
        return HttpResponse(f"{email1} {event_name}Ingrese sus datos de manera correcta\n :X")







# def index(request):asaasd
#     product_list = Producto.objects.order_by('nombre')[:6]
#     categorias  = Categoria.objects.order_by('nombre')
#     context = {'product_list': product_list, 'categorias': categorias}
#     return render(request,'index.html', context)

# def producto(request, producto_id):
#     producto = get_object_or_404(Producto, pk=producto_id)
#     categorias  = Categoria.objects.order_by('nombre')
#     context = {'producto' : producto, 'categorias': categorias}
#     return render(request,'producto.html', context)

# def products_by_category(request, name):
#     categoria = Categoria.objects.get(nombre = name)
#     products_by_category = categoria.producto_set.all()
#     categorias  = Categoria.objects.order_by('nombre')
#     context = {'products_by_category' : products_by_category , 'categorias': categorias}
#     return render (request,'categoria.html', context)