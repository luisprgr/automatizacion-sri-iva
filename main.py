import os
import json
import argparse
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from src.declaracion_iva import declaracion_iva


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=(
            "Aplicación para automatizar declaraciones del iva"
            " en el Servicio de Rentas Internas de Ecuador"
        )
    )

    parser.add_argument(
        "-c",
        "--guardar-capturas",
        help="Guarda capturas de pantalla de las acciones que ejecuta la app",
        action="store_true",
    )

    parser.add_argument(
        "-l",
        "--headless",
        help="Ejecuta la aplicación sin mostrar la interfaz de firefox",
        action="store_true",
    )

    args = parser.parse_args()

    app_data: dict = None
    guardar_capturas: bool = args.guardar_capturas
    headless: bool = args.headless
    tiempo_espera_segundos: int = 3

    if guardar_capturas:
        current_directory = os.getcwd()
        directorio_capturas = os.path.join(current_directory, 'capturas')
        if not os.path.isdir(directorio_capturas):
            os.mkdir(directorio_capturas)

    with open('datos.json') as f:
        app_data = json.load(f)

    if app_data is not None:
        tiempo_espera_segundos = app_data.get(
            'tiempo_espera_segundos', tiempo_espera_segundos)

        firefox_options = Options()
        firefox_options.headless = headless
        firefox = Firefox(options=firefox_options)
        firefox.set_window_size(1920, 1080)

        declaracion_iva(firefox, guardar_capturas,
                        tiempo_espera_segundos, app_data)

        firefox.close()
    else:
        print('no se pudo abrir datos.json')
