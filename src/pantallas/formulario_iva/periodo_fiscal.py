import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    TimeoutException,
)

from src.utilidades.utilidades import hover_and_click, guardar_captura
from src.pantallas.formulario_iva.ids import (
    OBLIGACION_DROPDOWN_ID,
    OBLIGACION_DECLARACION_IVA_2011_ELEMENT_ID,
    DIALOGO_DESCARTABLE_BUTTON_XPATH,
    DATE_SELECTOR_ID,
    DATE_ELEMENT_CSS_SELECTOR,
    PERIODO_FISCAL_SIGUIENTE_BUTTON_ID,
    DESCARTAR_BORRADOR_BUTTON_XPATH,
)


def seleccionar_periodo_fiscal(
    driver,
    guardar_capturas: bool,
    tiempo_espera: int,
    month: int,
    year: int
):

    wait = WebDriverWait(driver, 10)

    wait.until(expected.presence_of_element_located(
        (By.ID, OBLIGACION_DROPDOWN_ID)))

    time.sleep(tiempo_espera)

    hover_and_click(driver, OBLIGACION_DROPDOWN_ID)

    wait.until(expected.visibility_of_element_located(
        (By.ID, OBLIGACION_DECLARACION_IVA_2011_ELEMENT_ID)))

    declaration_2011 = driver.find_element(
        by=By.ID, value=OBLIGACION_DECLARACION_IVA_2011_ELEMENT_ID)
    
    declaration_2011.click()

    time.sleep(tiempo_espera)

    try:
        wait.until(expected.visibility_of_element_located((
            By.XPATH, DIALOGO_DESCARTABLE_BUTTON_XPATH))
        )

        discard_dialog_button = driver.find_element(
            By.XPATH,DIALOGO_DESCARTABLE_BUTTON_XPATH)
        
        discard_dialog_button.click()
    except ElementNotInteractableException:
        pass
    except TimeoutException:
        pass

    wait.until(expected.presence_of_element_located(
        (By.ID, DATE_SELECTOR_ID)))

    date_selector = driver.find_element(
        by=By.ID, value=DATE_SELECTOR_ID)
    date_selector.click()

    wait.until(expected.presence_of_element_located(
        (By.CSS_SELECTOR, DATE_ELEMENT_CSS_SELECTOR.format(month=month))))

    last_month_button = driver.find_element(
        by=By.CSS_SELECTOR, value=DATE_ELEMENT_CSS_SELECTOR.format(month=month))
    last_month_button.click()

    wait.until(expected.text_to_be_present_in_element_value(
        (By.ID, DATE_SELECTOR_ID), f'{month:02d}/{year}'))

    if guardar_capturas:
        guardar_captura(driver, 'seleccion_periodo_fiscal')

    next_step_button = driver.find_element(
        by=By.ID, value=PERIODO_FISCAL_SIGUIENTE_BUTTON_ID)
    next_step_button.click()

    time.sleep(tiempo_espera)

    try:
        discard_draft_button = driver.find_element(
            by=By.XPATH, value=DESCARTAR_BORRADOR_BUTTON_XPATH)
        discard_draft_button.click()
    except ElementNotInteractableException:
        pass
    except NoSuchElementException:
        pass
