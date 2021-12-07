from django.forms import ModelForm
from parking.models import Cliente
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(ModelForm):
    """
    Formulario para crear clientes
    """
    class Meta:
        model=Cliente
        fields = '__all__'

class RegistrationForm(UserCreationForm):
    '''
    Formulario para registrar usuarios
    '''
    class Meta:
        model = User
        fields = ['username','password1' ,'password2']



    
