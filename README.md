# grydd

# Requerimientos
Python 3 64bits

PostgreSQL

# Instrucciones
* Ejecute la consola de window `CMD`
* Crear en postgreSQL una base de datos llamada "grydd" (opcional para configuración de producción)
###
    create database grydd;
* Configurar los datos de conexión a la base de datos (name, user, y password) en la ruta `(grydd_project/.env)`
* Instalar python y agregarlo al path del sistema
* Instalar virtualevn
###
    pip install virtualenv
* Crear un nuevo entorno virtual de python por dentro de la ruta del proyecto `(grydd_project/env)`

Usando su version de python principal
###
    virtualenv env

O también puede utilizar un intérprete de Python de su elección
###
    virtualenv env -p c:\Python3\python.exe
* Active su entorno virtual
###
    env/Scripts/activate
* Regrese a la ruta principal del proyecto `(grydd_project/)`
* Instale los requerimientos del sistema
###
    pip install -r requirements.txt
* Instale las migraciones
###
    python manage.py migrate
* Agrupe los archivos estaticos
###
    python manage.py collectstatic
* Ejecute el servidor
###
    python manage.py runserver
