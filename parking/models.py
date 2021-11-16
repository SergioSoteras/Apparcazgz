from django.db import models

# Create your models here.
class Plaza(models.Model):
    '''
    La plaza de garaje
    '''
    planta = models.IntegerField(blank=False,null=False)
    numero = models.IntegerField(blank=False,null=False)

    def __str__(self):
        return f'{self.planta} {self.numero}'
    
    class Meta:
        pass

class Cliente(models.Model):
    '''
    El cliente
    '''
    dni = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=100)
    vehiculo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    class Meta:
        pass
class Disponibilidad(models.Model):
    '''
    Representa la plaza de garaje y el cliente que la tiene reservada
    '''
    plaza = models.ForeignKey(Plaza, on_delete=models.RESTRICT,)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, null=True, blank=True)
    
    LOAN_ESTADO = (
        ('d','Disponible'),
        ('nd','No disponible'),
    )

    estado = models.CharField(
        max_length=14,
        choices=LOAN_ESTADO,
        blank=False,
        default='Disponible',
        help_text='Disponibilidad',
    )

    class Meta:
        verbose_name='Estado de la plaza'
        verbose_name_plural='Estado de las plazas'
        ordering = ['plaza']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.plaza.numero} ({self.cliente})'

    class Meta:
        pass   
    
    