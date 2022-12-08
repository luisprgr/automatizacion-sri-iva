import time
from datetime import datetime

from src.utilidades.utilidades import guardar_captura
from src.pantallas.login.login import login_sri
from src.pantallas.formulario_iva.periodo_fiscal import (
    seleccionar_periodo_fiscal
)
from src.pantallas.formulario_iva.formulario import llenar_formulario
from src.pantallas.formulario_iva.preguntas import preguntas
from src.pantallas.comun.logout import logout_sri


def declaracion_iva(
    driver,
    guardar_capturas: bool,
    tiempo_espera: int,
    datos: dict,
    borrador: bool = True
):

    url_declaracion = datos['url_declaraciones']
    ruc = datos['ruc']
    password = datos['password']
    campos = datos['casillas']

    mes_anterior = datetime.now().month - 1
    año = datetime.now().year

    driver.get(url_declaracion)
    time.sleep(1)

    if guardar_capturas:
        guardar_captura(driver, 'inicio')

    login_sri(driver, guardar_capturas, ruc, password)

    seleccionar_periodo_fiscal(
        driver, guardar_capturas, tiempo_espera, mes_anterior, año)

    preguntas(driver, guardar_capturas)

    llenar_formulario(driver, guardar_capturas,
                      tiempo_espera, campos, borrador)

    logout_sri(driver, guardar_capturas)

    time.sleep(1)

    print(
        "La declaración se guardó exitosamente"
        f"{' como borrador' if borrador else ''}"
    )
