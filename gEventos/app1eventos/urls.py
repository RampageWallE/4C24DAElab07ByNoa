from . import views
from django.urls import path

urlpatterns = [
    path("", views.index , name='index'),
    path("validacion/", views.validacion, name='validacion'),
    #ADMIN
    path("admin/homepage", views.homepage_admin, name='homepage_admin'),
    path("admin/evento/crear", views.formulario_nuevo_evento, name='formulario_nuevo_evento'),
    path("admin/evento/crear/enviar", views.crear_evento, name='crear_evento'),
    path("admin/evento/modificar", views.formulario_modificar_evento, name='formulario_modificar_evento'),
    path("admin/evento/modificar/enviar", views.modificar_evento, name='modificar_evento'),
    path("admin/evento/borrar", views.borrar_evento, name='borrar_evento'),
    #CLIENTE 
    path("cliente/registro", views.formulario_registro, name='formulario_registro'),
    path("cliente/registro/save", views.guardar_usuario, name="guardar_usuario"),
    path("cliente/homepage", views.homepage_clien, name='homepage_clien'),
    path("cliente/evento/asistir", views.formulario_evento_asistir, name='formulario_evento_asistir'),
    path("cliente/evento/asistir/enviar", views.guardar_asistencia, name='guardar_asistencia'),
    #path('producto/<int:producto_id>/', views.producto, name='producto'),
    #path('categoria/<str:name>/', views.products_by_category, name='products_by_category')
]
