# CiceroT proyecto Web
A continuación se describen características del proyecto con el fin de facilitar la integración de CiceroT project en un ambiente de Desarrollo o Producción.

## Caracteristicas generales
El projecto se utiliza [python3.5]() y [Django1.10]()

## Desarrollo medgo
CiceroT esta creado en un ambiente de desarrollo creado con [vistualenv](), y el ambiente tiene el nombre de cicerotenv y se en activa mediante
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
CREATE USER cicerot@localhost IDENTIFIED BY 'cicerot';
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


