# Automatización-sri-iva

Automatización de declaraciones del IVA en el Servicio de Rentas Internas de Ecuador usando selenium  

:warning: este script actualmente está fallando debido a cambios en el sitio web del SRI. Se va a refactorizar el código con el estilo de manejo de ids de elementos web usado en [automatizacion-sri-facturas](https://github.com/luisprgr/automatizacion-sri-facturas) para hacer mas fácil la actualización de los ids en el futuro.


### Limitaciones actuales:
- Debe existir un ya una declaración anterior, en la cual se haya llenado el formulario de preguntas.
- Debido a que esta es una primera versión, el script está limitado a guardar la declaración como un borrador que luego debe ser aceptado manualmente por el usuario en el sitio web del SRI.

### Requerimientos:

- Python 3.10 o superior
- Poetry 1.2.2 o superior
- Firefox

### Instalación:

1. Clonar el repositorio

```bash
git clone https://github.com/luisprgr/automatizacion-sri-iva.git
```

2. Instalar dependencias

```bash
poetry install
```

3. Crear archivo con los datos para la declaración

```bash
cp datos.json.example datos.json
```

4. Editar el archivo `datos.json` con los datos de la declaración

### Ejecución:

- Ejecutar el script con su configuración de python por defecto mostrando el navegador y los pasos que está realizando

    ```bash
    poetry run python main.py
    ```

- Ejecutar el script en modo headless

    ```bash
    poetry run python main.py --headless
    ```

- Guardar capturas de pantalla de los pasos que realiza el script

    ```bash
    poetry run python main.py --guardar-capturas
    ```
    
    (este comando guarda las capturas en la carpeta `capturas` y puede ser combinado con el modo normal o headless)

- Ver la ayuda del script

    ```bash
    poetry run python main.py --help
    ```

### Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.


