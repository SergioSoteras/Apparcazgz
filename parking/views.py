from django.shortcuts import render

# Create your views here.
def contacto(request):
    '''
    Pagina de contacto de nuestra web
    '''
    datos = {'autor':'Sergio Soteras',
            'email': 'emaildecontacto@gmail.com',
            'fax': '976542198'}
    
    return render(request, 'contacto.html', context=datos)