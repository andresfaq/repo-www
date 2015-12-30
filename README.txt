1. Preliminares

	1.1 Tener instalado git [sudo apt-get install git]

	1.2 Tener instalado python3.4 [sudo apt-get install python3.4]

	1.4 Tener instalado virtualenv [sudo apt-get install python-virtualenv]

	1.5 Instalar las siguientes librerias [sudo apt-get install libpq-dev python-dev] y [sudo apt-get install python3.4-dev]

	1.6 Instalar mas librerias [sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \ libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk] #NUEVO!!!
	


2. Creando entorno virtual

	2.1 Se crea un entorno llamado env-www con python 3.4 [virtualenv -p /usr/bin/python3.4 env-www] 

	2.2 Se activa el entorno [source env-www/bin/activate]

	2.3 Se verifica la version de python dentro del entorno [python -V] debe ser python3.4


3. Instalando Django 1.8.4

	3.1 Se activa el entorno (ver punto 2.2)

	3.2 Se ingresa a la carpeta del entorno  [cd env-www]

	3.3 Se instala django 1.8.4 [pip install Django==1.8.4] 

	3.4 Se verifica la version de django [django-admin --version] debe aparecer 1.8.4
	
	3.5 instalar controlador de postgres para python [pip install psycopg2]

	3.6 instalar librerias para manejo de imagenes en los modelos de django [pip install Pillow] #NUEVO!!!


4. Instalando Base de datos PostgreSQL

	4.1 Instalar postgres [sudo apt-get install postgresql postgresql-contrib]

	4.2 Instalar administrador grafico (Opcional) [sudo apt-get install pgadmin3]

	4.3 Crear una base de datos llamada 'concesionario'
	



5. Instalando Proyecto

	5.1 Activar y entrar a la carpeta del entorno (Puntos 2.2 y 3.2)

	5.2 Clonar repositorio [git clone https://github.com/andresfaq/repo-www.git]
	
	5.3 Modificar el archivo settings.py en el directorio [ /repo-www/concesionario/concesionario]
	    en la seccion DATABASES y configurar los datos necesarios (Por ejemplo la contraseña o el usuario)

	5.4 Regresar al directorio  [/repo-www/concesionario] 

	5.5 Generar las migraciones [python manage.py makemigrations] #NUEVO!!! 

	5.6 Realizar la migracion de la base de datos [python manage.py migrate]

	5.7 Correr servidor [python manage.py runserver]

	5.8 Abrir navegador e ingresar a la direccion 127.0.0.1:8000 o localhost:8000 

#### NOTAS ####

[Problema cuando se ejecuta el comando 'git pull']
--> Si aparece algun error con archivos *.pyc cuando se realiza un pull del proyecto
    hay que ingresar por medio de la consola a la carpeta repo-www y ejecutar el siguiente comando
    [find . -name "*.pyc" -exec git rm -f {} \;] Luego hay que realizar un commit con los cambios 
    y por ultimo realizar de nuevo el pull del proyecto.   

[Solucionando problema de usuario postgres]
--> Si a la hora de configurar el servidor postgres en pgadmin3 aparece el siguiente error 
    "Error connecting to the server: FATAL:  password authentication failed for user "postgres"
    se puede solucionar con los siguientes comandos. 
    [sudo su postgres] luego [psql] y una vez dentro de la consola de postgres se escribe el siguiente comando 
    [alter user postgres with password 'MiNuevoPassword';]


### Otras anotaciones temporales ###

Actualicen sus proyectos realizando los pasos que tienen un "#NUEVO!!!" escrito al final


AÑADIR AL FINAL DEL ARCHIVO SETTINGS.PY
---
# Ruta donde se guardan las imagenes
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
--


	


	
