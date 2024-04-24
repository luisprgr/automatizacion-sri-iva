from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

from src.utilidades.utilidades import guardar_captura

from src.pantallas.formulario_iva.ids import PREGUNTAS_SIGUIENTE_BUTTON_ID

def preguntas(
    driver,
    guardar_capturas: bool,
):

    wait = WebDriverWait(driver, 10)

    wait.until(expected.presence_of_element_located(
        (By.ID, PREGUNTAS_SIGUIENTE_BUTTON_ID)))

    if guardar_capturas:
        guardar_captura(driver, 'preguntas')

    import time
    time.sleep(5)

    next_step_button = driver.find_element(
        by=By.ID, value=PREGUNTAS_SIGUIENTE_BUTTON_ID)
    next_step_button.click()
