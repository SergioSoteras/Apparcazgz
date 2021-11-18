from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from parking.models import *
from parking.forms import *

# Create your views here.
#contacto
def contacto(request):
    '''
    Pagina de contacto de nuestra web
    '''
    datos = {'autor':'Sergio Soteras',
            'email': 'emaildecontacto@gmail.com',
            'fax': '976542198'}
    
    return render(request, 'contacto.html', context=datos)

#indice
def indice(request):
    '''
    Pagina inicial de nuestra web
    '''
    num_disponibles = 0
    disponibles = Disponibilidad.objects.all()
    for disp in disponibles:
            if (disp.estado == 'd'):
                    num_disponibles += 1

    
    datos = {'autor':'Sergio Soteras',
            'num_disponibles': num_disponibles,
            }

    # Number of visits to this view, as counted in the session variable.
    visitas = request.session.get('visitas', 0)
    request.session['visitas']= visitas + 1
    datos['visitas'] = visitas
    return render(request, 'index.html', context=datos)

#vista de un cliente
class ClienteDetailView(generic.DetailView):
    model = Cliente

#lista clientes
class ClientesListView(generic.ListView):
    '''
    Vista generica para nuestro listado de clientes
    '''
    model = Cliente
    paginate_by = 10

#crear cliente con funcion
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente creado.')
            return redirect('/parking/clientes/')
    else:
        form = ClienteForm()
    datos = {'form': ClienteForm()}
    return render(request, 'crear_cliente.html', 
        context=datos)

#crear cliente con generic
class CrearCliente(SuccessMessageMixin, generic.CreateView):
    model = Cliente
    form_class = ClienteForm
    
    template_name = 'crear_cliente.html'
    success_url = '/parking/clientes/'
    success_message = "%(nombre)s %(apellidos)s se ha creado correctamente"

# Modificar y Eliminar Cliente con SuccessMesaageMixin para mensaje de éxito.
class ModificarCliente(SuccessMessageMixin, generic.UpdateView):
    model = Cliente
    fields = '__all__'
    
    template_name = 'modificar_cliente.html'
    success_url = '/parking/clientes/'
    success_message = "%(nombre)s %(apellidos)s se ha modificado correctamente"

class EliminarCliente(generic.DeleteView):
    model = Cliente
    template_name = 'cliente_confirmar_borrado.html'
    success_url = '/parking/clientes/'
    success_message = "El cliente se ha borrado correctamente"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarCliente, self).delete(request, *args, **kwargs)

#vista de disponibilidad
class DisponibilidadDetailView(generic.DetailView):
    model = Disponibilidad
    
#lista disponibilidad
class DisponibilidadListView(generic.ListView):
    '''
    Vista generica para nuestra lista de disponibilidad de las plazas
    '''
    model = Disponibilidad
    paginate_by = 15

# Modificar Disponibilidad con SuccessMesaageMixin para mensaje de éxito.
#Solo el admin, debes estar logueado
#@login required
class ModificarDisponibilidad(SuccessMessageMixin, generic.UpdateView):
    model = Disponibilidad
    fields = '__all__'
    template_name = 'modificar_disponibilidad.html'
    success_url = '/'
    success_message = "%(plaza)s  se ha modificado correctamente"