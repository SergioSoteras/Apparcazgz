from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from parking.models import *
from parking.forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.hashers import make_password

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
    todas_plazas = Plaza.objects.all()
    for plaza in todas_plazas:
            if (plaza.disponible()):
                    num_disponibles += 1

    
    datos = {'autor':'Sergio Soteras',
            'num_disponibles': num_disponibles,
            'coords': '41.6524426,-0.8855355',
            }

    # Number of visits to this view, as counted in the session variable.
    visitas = request.session.get('visitas', 0)
    request.session['visitas']= visitas + 1
    datos['visitas'] = visitas
    return render(request, 'index.html', context=datos)

#vista de un cliente
class ClienteDetailView(LoginRequiredMixin,generic.DetailView):
    model = Cliente

#lista clientes
class ClientesListView(LoginRequiredMixin, generic.ListView):
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
class CrearCliente(LoginRequiredMixin,PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Cliente
    form_class = ClienteForm
    permission_required = 'parking.add_cliente'
    
    template_name = 'crear_cliente.html'
    success_url = '/parking/clientes/'
    success_message = "%(nombre)s %(apellidos)s se ha creado correctamente"

# Modificar y Eliminar Cliente con SuccessMesaageMixin para mensaje de éxito.
class ModificarCliente(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, generic.UpdateView):
    model = Cliente
    fields = '__all__'
    permission_required = 'parking.change_cliente'
    template_name = 'modificar_cliente.html'
    success_url = '/parking/clientes/'
    success_message = "%(nombre)s %(apellidos)s se ha modificado correctamente"

class EliminarCliente(LoginRequiredMixin,PermissionRequiredMixin,generic.DeleteView):
    model = Cliente
    template_name = 'cliente_confirmar_borrado.html'
    success_url = '/parking/clientes/'
    success_message = "El cliente se ha borrado correctamente"
    permission_required = 'parking.delete_cliente'
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarCliente, self).delete(request, *args, **kwargs)


#lista plazas
class PlazaListView(generic.ListView):
    '''
    Vista generica para nuestra lista de disponibilidad de las plazas
    '''
    model = Plaza
    paginate_by = 27

#Buscador de clientes por apellidos o nombre
class SearchResultsListView(LoginRequiredMixin,ListView):
    model = Cliente
    context_object_name = 'clientes'
    template_name = 'search_results.html'  # No usará la plantilla estándar del ListView
    paginate_by = 25


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        query2 = self.request.GET.get('q2')
        if query:
            return Cliente.objects.filter(apellidos__icontains=query)
        elif query2:
            return Cliente.objects.filter(nombre__icontains=query2)
        else:
            return []


#Funcion para crear users desde la web.
def crear_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db
            user.save()
            raw_password = form.cleaned_data.get('password1')
            messages.add_message(request, messages.SUCCESS,'Usuario creado.')
            return redirect('/')
    else:
        form = RegistrationForm()   
    return render(request, 'registrar.html', {'form':form})

