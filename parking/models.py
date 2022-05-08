from django.db import models

# Create your models here.
class Dimensiones(models.Model):
    '''
    Las dimensiones de la plaza de garaje
    '''
    tipo = models.CharField(primary_key=True, max_length=8)
    altura = models.IntegerField(blank=False,null=False)
    anchura = models.DecimalField(max_digits=3,decimal_places=2,blank=False,null=False)
    largura = models.DecimalField(max_digits=3,decimal_places=2,blank=False,null=False)

    def __str__(self):
        return f'{self.tipo} ({self.largura}m x {self.anchura}m x {self.altura}m)'

    class Meta:
        pass

class Plaza(models.Model):
    '''
    La plaza de garaje
    '''
    planta = models.IntegerField(blank=False,null=False)
    numero = models.IntegerField(blank=False,null=False)
    dimensiones = models.ForeignKey(Dimensiones, on_delete=models.RESTRICT,null=True,blank=True)

    def __str__(self):
        return f'Plaza {self.numero} ( Planta {self.planta} )'
    
    def disponible(self):
        if len(self.cliente_set.all()) > 0 :
            return False
        else:
            return True
    def nombre_cliente(self):
        if len(self.cliente_set.all()) > 0 :
            return self.cliente_set.first()
        else:
            return ''
    def limit_plazas():
        plazas_disp =[]
        todas_plazas = Plaza.objects.all()
        for plaza in todas_plazas:
            if (plaza.disponible()):
                plazas_disp.append(plaza)
        return plazas_disp

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
    plaza = models.ForeignKey(Plaza, on_delete=models.RESTRICT,unique=True,null=True,blank=True) 

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    
    class Meta:
        pass

class Disponibilidad(models.Model):
    '''
    Ya no la uso porque no me hace falta, pero si la elimino me da errores.
    '''
    plaza = models.ForeignKey(Plaza, on_delete=models.RESTRICT,)
    class Meta:
        verbose_name='Estado de la plaza'
        verbose_name_plural='Estado de las plazas'
        ordering = ['plaza']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.plaza.numero} ({self.cliente})'

    class Meta:
        pass   
    
