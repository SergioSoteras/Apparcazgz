from django.urls import include,path
from parking.views import *

urlpatterns = [
    path('clientes/', ClientesListView.as_view(), name='listado_clientes'),
    path('plazas/', PlazaListView.as_view(), name='listado_plazas'),
    path('cliente/modificar/<str:pk>', ModificarCliente.as_view(), name='modificar_cliente'),
    path('cliente/eliminar/<str:pk>', EliminarCliente.as_view(), name='eliminar_cliente'),
    path('cliente/crear', CrearCliente.as_view(), name='crear_cliente'),
    path('cliente/crear2', crear_cliente, name="crear_cliente2"),
    path('cliente/<str:pk>', ClienteDetailView.as_view(), name='info_cliente'),
    path('buscaclientes/', SearchResultsListView.as_view(),name="buscaclientes" ),
    path('descarga_clientes', descarga_csv_clientes, name="descarga_clientes"),

]
