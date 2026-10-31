Repositorio para Proyecto de Reportes sobre Patrimonio

Para hacer uso del proyecto se debe seguir las siguientes indicaciones:

1. Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

    Python 3.12 (o la versión que uses)
    pip
    Git

2. Clonar el repositorio

git clone https://github.com/usuario/nombre-repositorio.git
cd nombre-repositorio

3. Crear y activar entorno virtual
Windows

python -m venv venv
venv\Scripts\activate

Linux/macOS

python3 -m venv venv
source venv/bin/activate

4. Instalar dependencias

pip install -r requirements.txt

5. Aplicar migraciones

python manage.py migrate

6. Crear usuario administrador (opcional):

python manage.py createsuperuser

7. Ejecutar el servidor

python manage.py runserver

La aplicación estará disponible en:

http://127.0.0.1:8000/

Funcionalidad "Corazón"

Para probar la funcionalidad de favoritos:

    Registrar y/o Iniciar sesión con un usuario.
    Ir a la sección "Reportes".
    Rellenar lo que se pide y enviar el reporte.
    Verificar que se haya creado correctamente el Reporte.

Estructura del proyecto

reportesproyecto/
│
├── assets/
├── posts/
├── reportesproyecto/
├── static/
├── templates/
├── users/
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
