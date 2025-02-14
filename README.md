# Automatización-sri-iva

Automatización de la declaración del IVA en el Servicio de Rentas Internas (SRI) de Ecuador usando selenium  

### Limitaciones actuales:
- Actualmente no se cambian valores del formulario de preguntas, solo se llenan los valores de la declaración.
- El script se limita a guardar la declaración como un borrador una vez que esta ha sido completada. El usuario debe acceder al portal del SRI para revisarla y enviarla manualmente.

### Requerimientos:

- Python 3.13 o superior
- Firefox

### Requerimientos opcionales: 

- [uv](https://docs.astral.sh/uv/) 

### Instalación:

1. Clonar el repositorio

    ```bash
    git clone https://github.com/luisprgr/automatizacion-sri-iva.git
    ```

2. Instalar dependencias

    ##### Si `uv` está instalado:

    ```bash
    uv sync
    ```

    ##### O mediante `venv` + `pip`:

    Creamos un entorno virtual
    
    ```bash
    python -m venv .venv
    ```

    Activamos el entorno virtual (en Windows):

    ```Powershell
    .venv\Scripts\activate
    ```

    Activamos el entorno virtual (en macOS/Linux):

    ```bash
    source .venv/bin/activate
    ```

    Finalmente, instalamos las dependencias con:
    ```bash
    pip install .
    ````


3. Crear archivo con los datos para la declaración

    ```bash
    cp datos.json.example datos.json
    ```

4. Editar el archivo `datos.json` con los datos de la declaración

### Ejecución:

- Ejecutar el script con su configuración por defecto (muestra las acciones que se realizan el navegador):

    Con uv:

    ```bash
    uv run main.py
    ```

    O ejecutando dentro del entorno virtual creado anteriormente:

    ```bash
    python3 main.py
    ```

- Ejecutar el script en modo headless:

    ```bash
    uv run main.py --headless
    ```

    O 

    ```bash
    python3 main.py --headless
    ```

- Guardar capturas de pantalla de las acciones realizadas por el script

    ```bash
    uv run main.py --guardar-capturas
    ```

    O 

    ```bash
    python3 main.py --guardar-capturas
    ```
    
    (este comando guarda las capturas de pantalla en una carpeta llamada `capturas` y puede ser combinado con el modo normal o headless)

- Ver la ayuda del script

    ```bash
    uv run main.py --help
    ```

    O 

    ```bash
    python3 main.py --help
    ```

### Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.


