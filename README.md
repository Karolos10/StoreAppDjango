# ProyectoWeb

Este es un proyecto Django llamado **ProyectoWeb** que incluye una aplicación de tienda llamada **ProyectoWebApp**.

## Descripción

**ProyectoWeb** es una aplicación de tienda en línea desarrollada con Django. Permite a los usuarios navegar por productos, agregarlos al carrito y realizar compras.

## Requisitos

- Python 3.x
- Django 3.x 5.1.1

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Karolos10/StoreAppDjango.git
    cd ProyectoWeb
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    env\Scripts\activate  # En Windows
    # source env/bin/activate  # En macOS/Linux
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

5. Carga datos iniciales (opcional):

    ```bash
    python manage.py loaddata initial_data.json
    ```

6. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

7. Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Estructura del Proyecto

## Funcionalidades

- Navegación por productos
- Carrito de compras
- Proceso de pago
- Gestión de usuarios

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Crea un Pull Request.

## Licencia