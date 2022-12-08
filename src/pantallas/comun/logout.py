from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

from src.utilidades.utilidades import guardar_captura


def logout_sri(driver, guardar_capturas: bool):

    wait = WebDriverWait(driver, 10)

    driver.get(
        'https://srienlinea.sri.gob.ec'
        '/sri-declaraciones-web-internet/pages/salir.jsp')

    wait.until(expected.presence_of_element_located((By.ID, 'usuario')))

    if guardar_capturas:
        guardar_captura(driver, "logout")
