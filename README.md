# CiceroT proyecto Web
A continuación se describen características del proyecto con el fin de facilitar la integración de CiceroT project en un ambiente de Desarrollo o Producción.

## Caracteristicas generales
El projecto se utiliza [python3.5]() y [Django1.10]() y [Mysql5.5.55]()
## Desarrollo medgo
CiceroT esta creado en un ambiente de desarrollo creado con [vistualenv](), y el ambiente tiene el nombre de cicerotenv y se en activa mediante

- Actualizar header
	```
	sudo apt-get update
	```
- Instalar virtualenv
	```
	sudo apt-get install virtualenv python-virtualenv
	```
- Crear directorio del proyecto
	```
	mkdir CiceroT 
	```
- Crear entorno virtual para proyecto con python versión 3 (por defecto 2.7)
	```
	virtualenv -p python3 cicerotenv
	```
- Activar entorno virtual (estando en el directorio cicerotenv)
	```
	source bin/activate
	```

- [Agregar SSH a github](https://help.github.com/articles/connecting-to-github-with-ssh/)
- CLONAR PROYECTO
- En la carpeta del proyecto (con python 3 o pip3)
	```
	pip install -r requirements.txt
	```
	

- Activar
```
cd ~/medgochile
source cicerotenv/bin/activate
```
- Desactivar
```
deactivate
```

### Config Mysql
Configuración para Mysql y Django
```
mysql -u root -p
CREATE DATABASE cicerot CHARACTER SET UTF8;
CREATE USER cicerot@localhost IDENTIFIED BY 'cicerotpiinfo';
GRANT ALL PRIVILEGES ON cicerot.* TO cicerot@localhost;
```
Migración: En directorio cicerotproject
```
python manage.py makemigrations
python manage.py migrate
```

### Django
```

```
### Instalación de requerimientos: En directorio cicerotproject
```
pip3 install -r requirements.txt
```

## Produccion medgo

# Comandos importantes
## Correr servidor desarrollo local
```
python3 manage.py runserver
```


