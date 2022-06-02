## Apparking
El proyecto Apparking es una aplicación web que nace de la necesidad de una comunidad de gestionar su aparcamiento subterráneo, que ofrece al administrador la posibilidad de distribuir las plazas de aparcamiento y los clientes.

El funcionamiento de la aplicación comienza con el superuser, al que se ha llamado admin, el cual tendrá acceso al panel de control del admin añadiendo /admin al path, donde podrá crear las plazas, clientes y dimensiones de las plazas. También dispone de un formulario en la aplicación para crear clientes de manera más sencilla y rápida.

Los clientes podrán visualizar el plano del aparcamiento en directo, donde podrán comprobar cuantas plazas quedan disponibles, comprobar el cliente de una plaza ocupada y el listado de clientes del aparcamiento.

********

The main purpose of ‘Apparking’ is to offer a tailored management of a parking lot in a quick and easy way.

It allows a single customisation of the parking lot adjusted to the layout of the parking spaces, which makes the application unique and innovative. You can check the availability of parking spaces at a glance and find out which customer is occupying them.

You are also one click away from checking the customers in the parking lot, seeing their details and editing them.

It has a role-based access control (RBAC) based on a security function to control user access to tasks usually restricted to the superuser (admin).

Currently, only the admin can modify the application data, but in the future, it will have a payment gateway so that users can also book and pay for their parking slots.

********
## MANUAL DE INSTALACIÓN
1. Instalacion de Python

  - Descargaremos la version python 3.10 o superior

  - <https://www.python.org/downloads>

2. Creamos un Entorno Virtual
- Linux :

  sudo apt-get install python3-venv

  python3 –m venv env

- macOS :

  python3 –m venv env

- Windows :

  python –m venv env

3. Activar el Entorno Virtual
- Linux / Mac :

  source env/bin/activate

- Windows :

  env\Scripts\activate.bat

4. Instalar Django y dependencias

  - pip install Django

  - pip install requirements.txt

5. Crear superuser

  - py manage.py createsuperuser

  - Es importante que el username sea ***admin***

6. py manage.py runserver

