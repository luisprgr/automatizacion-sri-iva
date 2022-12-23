from typing import Dict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from src.utilidades.utilidades import (
    hover_and_click,
    guardar_captura,
    scroll_to_bottom
)


def id_casilla(number: int, driver) -> str:
    return driver.find_element(
        by=By.XPATH, value=f"//label[contains(text(), '{number}')]"
    ).get_attribute('data-referencia').split('.')[0]


def llenar_formulario(
    driver,
    guardar_capturas: bool,
    tiempo_espera: int,
    campos: Dict[str, float],
    borrador: bool = True
):

    wait = WebDriverWait(driver, 10)

    wait.until(expected.presence_of_element_located(
        (By.XPATH, "//div[@id='frmFlujoDeclaracion:pnlFormularioExtendido_content']")))

    formulario_id = driver.find_element(
        By.XPATH, "//div[@id='frmFlujoDeclaracion:pnlFormularioExtendido_content']/div/div").get_attribute('id').split(':')[1].replace('j_idt', '')
    
    # Abre todas las secciones

    # Sección de ventas
    hover_and_click(driver, f'frmFlujoDeclaracion:j_idt{formulario_id}:2:seccion')
    scroll_to_bottom(driver)
    wait.until(expected.visibility_of_element_located(
        (By.ID, f'frmFlujoDeclaracion:j_idt{formulario_id}:2:seccion:seccion-tab')))

    # Sección de resumen impositivo
    hover_and_click(driver, f'frmFlujoDeclaracion:j_idt{formulario_id}:6:seccion')
    scroll_to_bottom(driver)
    wait.until(expected.visibility_of_element_located(
        (By.ID, f'frmFlujoDeclaracion:j_idt{formulario_id}:6:seccion:seccion-tab')))

    # Sección de devolucion del isd
    hover_and_click(driver, f'frmFlujoDeclaracion:j_idt{formulario_id}:8:seccion')
    scroll_to_bottom(driver)
    wait.until(expected.visibility_of_element_located(
        (By.ID, f'frmFlujoDeclaracion:j_idt{formulario_id}:8:seccion:seccion-tab')))

    # Sección de totales
    hover_and_click(driver, f'frmFlujoDeclaracion:j_idt{formulario_id}:12:seccion')
    scroll_to_bottom(driver)
    wait.until(expected.visibility_of_element_located(
        (By.ID, f'frmFlujoDeclaracion:j_idt{formulario_id}:12:seccion:seccion-tab')))

    # Llena los campos

    for casilla, valor in campos.items():

        casilla_id = id_casilla(casilla, driver)

        casilla_input = driver.find_element(by=By.ID, value=casilla_id)

        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'auto',block: 'center',inline: 'center'})",
            casilla_input.find_element(by=By.XPATH, value='..')
        )

        scroll = ActionChains(driver)

        scroll.move_to_element(casilla_input).perform()

        casilla_input.click()

        [casilla_input.send_keys(Keys.DELETE) for _ in range(10)]

        casilla_input.send_keys(valor)

    if guardar_capturas:
        guardar_captura(driver, 'formulario_llenado')

    # Guarda la declaración

    if borrador:
        save_button = driver.find_element(
            by=By.XPATH, value="//button/span[contains(text(), 'Guardar borrador')]")
        save_button.click()
