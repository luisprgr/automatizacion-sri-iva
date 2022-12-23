import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

from src.utilidades.utilidades import hover_and_click, guardar_captura


def seleccionar_periodo_fiscal(
    driver,
    guardar_capturas: bool,
    tiempo_espera: int,
    month: int,
    year: int
):

    wait = WebDriverWait(driver, 10)
    wait.until(expected.presence_of_element_located(
        (By.ID, 'frmFlujoDeclaracion:somObligacion_label')))

    time.sleep(tiempo_espera)

    hover_and_click(driver, 'frmFlujoDeclaracion:somObligacion_label')

    wait.until(expected.visibility_of_element_located(
        (By.ID, 'frmFlujoDeclaracion:somObligacion_1')))

    declaration_2011 = driver.find_element(
        by=By.ID, value='frmFlujoDeclaracion:somObligacion_1')
    declaration_2011.click()

    time.sleep(tiempo_espera)

    wait.until(expected.visibility_of_element_located(
        (By.XPATH, "//div[@id='frmFlujoDeclaracion:dialogoMensajesPersonalizados']//button[contains(@id, 'frmFlujoDeclaracion')]")))

    rimpe_discard_button = driver.find_element(
        By.XPATH, "// div[@id='frmFlujoDeclaracion:dialogoMensajesPersonalizados']//button[contains(@id, 'frmFlujoDeclaracion')]")
    rimpe_discard_button.click()

    wait.until(expected.presence_of_element_located(
        (By.ID, 'frmFlujoDeclaracion:calPeriodo')))

    date_selector = driver.find_element(
        by=By.ID, value='frmFlujoDeclaracion:calPeriodo')
    date_selector.click()

    wait.until(expected.presence_of_element_located(
        (By.CSS_SELECTOR, f'a.button-{month}')))

    last_month_button = driver.find_element(
        by=By.CSS_SELECTOR, value=f'a.button-{month}')
    last_month_button.click()

    wait.until(expected.text_to_be_present_in_element_value(
        (By.ID, 'frmFlujoDeclaracion:calPeriodo'), f'{month:02d}/{year}'))

    if guardar_capturas:
        guardar_captura(driver, 'seleccion_periodo_fiscal')

    next_step_button = driver.find_element(
        by=By.ID, value='frmFlujoDeclaracion:btnObligacionSiguiente')
    next_step_button.click()

    time.sleep(tiempo_espera)

    try:
        discard_draft_button = driver.find_element(
            by=By.XPATH, value="//button/span[contains(text(), 'Rechazar')]")
        discard_draft_button.click()
    except ElementNotInteractableException:
        pass
    except NoSuchElementException:
        pass
