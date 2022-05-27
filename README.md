Apparking
Se trata de una aplicación web que gestiona un parking para una comunidad de vecinos, en el que puedes comprobar cuantas plazas hay disponibles y los clientes que tiene.

Para poder ver los clientes del parking, es necesario hacer login.

Únicamente el admin puede crear, modificar o añadir clientes así como gestionar las plazas disponibles, de hecho, la página web tiene restringida muchas opciones de accesos rápidos a la hora de gestionar los clientes y las plazas al usuario admin.


********
## MANUAL DE INSTALACIÓN
1. Instalacion de Python

  Descargaremos la version python 3.10 o superior

  <https://www.python.org/downloads>

1. Creamos un Entorno Virtual
- Linux :

  sudo apt-get install python3-venv

  python3 –m venv env

- macOS :

  python3 –m venv env

- Windows :

  python –m venv env

1. Activar el Entorno Virtual
- Linux / Mac :

  source env/bin/activate

- Windows :

env\Scripts\activate.bat

1. Instalar Django y dependencias

  pip install Django

  pip install requirements.txt

1. Crear superuser

  py manage.py createsuperuser

  Es importante que el username sea admin

1. py manage.py runserver

