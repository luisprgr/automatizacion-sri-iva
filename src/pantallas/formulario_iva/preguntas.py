from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

from src.utilidades.utilidades import guardar_captura


def preguntas(
    driver,
    guardar_capturas: bool,
):

    wait = WebDriverWait(driver, 10)

    wait.until(expected.presence_of_element_located(
        (By.ID, 'frmFlujoDeclaracion:btnPerfiladorSiguiente')))

    if guardar_capturas:
        guardar_captura(driver, 'preguntas')

    next_step_button = driver.find_element(
        by=By.ID, value='frmFlujoDeclaracion:btnPerfiladorSiguiente')
    next_step_button.click()
