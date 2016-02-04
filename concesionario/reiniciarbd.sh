# Reiniciador de la base de datos
# Reemplazen el nombre de usuario
# Ejecuten haciendo [sh reiniciarbd.sh] en consola
sudo -u postgres psql -c 'DROP DATABASE concesionario;'
sudo -u postgres psql -c 'CREATE DATABASE concesionario WITH OWNER postgres;'
sudo -u postgres psql -c 'GRANT ALL PRIVILEGES ON DATABASE concesionario TO postgres;'
python manage.py migrate auth
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
python manage.py shell < administracion/seeders.py
python manage.py runserver