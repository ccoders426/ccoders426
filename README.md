# Proyecto Coder

Este proyecto trae consigo la construcción de un sitio web, tras conocimientos básicos adquiridos de ***python***, ***django***, ***html***, ***css***, ***js*** y ***DB*** con ***sqlite3*** hasta la ***clase 22*** del curso ***python***, ***comisión 54125*** - ***coder house***

## Proceso de construcción del proyecto

> - [x] Se crea carpeta raiz del proyecto con el código: ***django-admin startproject [nombre del proyecto]***
> - [x] Se accede a la carpeta recien creada con el paso anterior. se crea la aplicación con el código:  ***django-admin startapp [nombre de la aplicación]*** o ***python manage.py startapp [nombre de la aplicación]***

## Proceso de construcción de la DB

> - [x] Se establece en el archivo ***models.py*** de la aplicación la estructura, ***(campos, atributos, tipos y parametros)*** de la DB.
> - [x] Se valida el estado de la aplicación con el código ***python manage.py check [nombre de la aplicación]***
> - [x] Se construye el borrador (crear migraciones a la DB) de la estrutura de la DB y tablas que la componen con el código ***python manage.py makemigrations***.
> - [x] Se hacen las migraciones a la DB con el código ***python manage.py migrate*** con la que se crea la DB sqliite3 y se observan en los campos los atributos de las clases definidas en el ***models.py***. Este a su vez crea una carpeta llamada ***migrations*** donde se almacena los archivos de la DB.

## Creación de carpetas y archivos

> Una vez terminado el proceso anterior, se procede a crear las carpetas y archivos detallados a continuación:

> carpetas

- [x] ***Carpeta templates*** donde se almacenan todos los archivos archivos **.html** del proyecto.
- [x] ***Carpeta static*** y otra dentro de esta ***[Con el nombre de la aplicación]*** donde se almacenan todos los archivos restantes del sitio web como **.css**, **.js**, **imagenes**, entre otros.

> archivos

- [x] En la **carpeta de la App** se debe crear el archivo ***urls.py*** donde se almacenan las URLs de la aplicación del proyecto.
- [x] En la **carpeta templates de la App** se debe crear los archivos ***.html*** los cuales son para las páginas del sitio web.
- [x] En la carpeta de la App se debe crear el archivo ***forms.py*** en el que se almacenan las configuraciones de los formularios.

## Configuraciones

> Se añaden en el archivo ***settings.py*** tanto la aplicación como la ruta de donde se van a tomar los templates.

> En el archivo ***models.py*** en el que se encentran cada una de las estructuras de los campos y criterios que deben tener los datos en las tablas de la DB 

> En el archivo de las ***urls.py*** de la **aplicación** como del **proyecto** se añaden cada una de las **URLs** que requieren para redireccionamientos entre los archivos **.html** y cada una de las funciones en las **vistas**.

> En el archivo ***views.py*** se encuentran todas las vistas basadas en funciones del proyecto, va muy de la mano con el archivo ***url.py***  

> En el archivo ***admin.py*** se almacena el registro de cada uno de los **models** para su respectiva gestión, donde se pueden ***delegar permisos***, ***roles*** y ***privilegios*** a los ***usuarios*** en el proyecto.

> En el archivo ***forms.py*** en el que se almacenan las configuraciones de los campos y criterios en los ***formularios***.

>> Cabe resaltar que se hace el llamado de cada uno de los modulos requeridos por cada archivo y respectiva función.

> Por el lado de los archivos ***.html***, se construyen las diferentes páginas del sitio haciendo uso de los recursos como lo son ***css***, ***js***, entre otros. 
