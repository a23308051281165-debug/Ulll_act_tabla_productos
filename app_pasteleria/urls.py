from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_pasteleria, name='inicio_pasteleria'),
    path('productos/agregar/', views.agregar_pasteleria, name='agregar_pasteleria'),
    path('productos/crear/', views.realizar_actualizacion_pasteleria, name='realizar_actualizacion_pasteleria'),
    path('productos/<int:pk>/editar/', views.actualizar_pasteleria, name='actualizar_pasteleria'),
    path('productos/<int:pk>/editar/guardar/', views.realizar_actualizar_producto, name='realizar_actualizar_producto'),
    path('productos/<int:pk>/borrar/', views.borrar_pasteleria, name='borrar_pasteleria'),
    path('productos/<int:pk>/borrar/confirmar/', views.realizar_borrar_pasteleria, name='realizar_borrar_pasteleria'),
    path('ver_producto/<int:id_producto>/', views.ver_producto, name='ver_producto'),
]
