# Sistema de Reportes sobre Patrimonio Cultural de Valparaíso
**Aplicación web desarrollada con *Django* que permite a los usuarios registrar reportes patrimoniales georreferenciados, adjuntar imágenes, clasificarlos por categoría y exportar la información en formato Excel junto con las imágenes asociadas.**

## Características
+ Registro e inicio de sesión de usuarios.
+ Creación de reportes patrimoniales.
+ Adjuntar imágenes a los reportes.
+ Registro de ubicación mediante coordenadas geográficas.
+ Clasificación por categorías patrimoniales.
+ Visualización detallada de reportes.
+ Exportación de reportes a Excel (.xlsx).
+ Exportación de imágenes y datos en un archivo comprimido (.zip).
+ Hoja de resumen con estadísticas generales.
+ Enlaces directos a Google Maps para cada reporte.
## Requisitos
+ *Python* 3.14 o superior.
+ *Django* 6.1.2.
+ *Pillow*.
+ *OpenPyXL*.
## Instalación
### 1. Clonar el repositorio
`git clone` https://github.com/MinaRii09/Proyecto-inicial-PY.git

`cd reportesproyecto`

### 2. Crear un entorno virtual
Windows:

`python -m venv venv`

venv\Scripts\activate

Linux / macOS:

`python3 -m venv venv`

`source venv/bin/activate`

### 3. Instalar dependencias
`pip install -r` requirements.txt

Si no existe el archivo *requirements.txt*, instalar manualmente:

`pip install` django

`pip install` pillow

`pip install` openpyxl

### 4. Aplicar migraciones
`python manage.py migrate`

### 5. Crear un usuario administrador
`python manage.py createsuperuser`

**Completar los datos solicitados por consola.**

### 6. Ejecutar el servidor
`python manage.py runserver`

**Abrir en el navegador:**

http://127.0.0.1:8000/ o http://localhost:8000/
 
## Estructura de Archivos

### Archivos estáticos
*static/*

**Contiene hojas de estilo, imágenes y archivos JavaScript.**

### Archivos subidos por usuarios
*media/*

**Contiene las imágenes asociadas a los reportes.**

### Base de datos
*db.sqlite3*

**Base de datos SQLite utilizada durante el desarrollo.**

### Exportación de Reportes
**Los reportes pueden exportarse a un archivo comprimido .zip que contiene:**

reports_export.zip

│

├── reports.xlsx

│

└── images/

├── report_0001_imagen.jpg

├── report_0002_imagen.jpg

└── ...

## El archivo Excel incluye:
+ Datos de cada reporte.
+ Usuario que realizó el reporte.
+ Fecha de creación.
+ Categoría patrimonial.
+ Coordenadas geográficas.
+ Enlace directo a *Google Maps*.
+ Hoja de resumen con estadísticas generales.

## Tecnologías Utilizadas
+ *Python*
+ *Django*
+ *SQLite*
+ *OpenPyXL*
+ *Pillow*
+ *HTML*
+ *CSS*
+ *JavaScript*
### Hecho por Grupo 8 "SalvaRamos"

<img src="reportesproyecto/static/images/v4o8ngkvx9th1.jpeg" width="200">
