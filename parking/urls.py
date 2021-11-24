from django.urls import include,path
from parking.views import *

urlpatterns = [
    path('clientes/', ClientesListView.as_view(), name='listado_clientes'),
    path('disponibilidad/', DisponibilidadListView.as_view(), name='listado_disponibilidad'),
    path('plazas/', PlazaListView.as_view(), name='listado_plazas'),
    path('cliente/modificar/<str:pk>', ModificarCliente.as_view(), name='modificar_cliente'),
    path('cliente/eliminar/<str:pk>', EliminarCliente.as_view(), name='eliminar_cliente'),
    path('cliente/crear', CrearCliente.as_view(), name='crear_cliente'),
    path('cliente/crear2', crear_cliente, name="crear_cliente2"),
    path('cliente/<str:pk>', ClienteDetailView.as_view(), name='info_cliente'),
    path('disponibilidad/<int:pk>', DisponibilidadDetailView.as_view(), name="info_disponibilidad"),
    path('disponibilidad/modificar/<int:pk>', ModificarDisponibilidad.as_view(), name='modificar_disponibilidad'),
    path('buscaclientes/', SearchResultsListView.as_view(),name="buscaclientes" ),

]
