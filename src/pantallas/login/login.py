from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

from src.utilidades.utilidades import guardar_captura


def login_sri(driver, guardar_capturas: bool, ruc: str, password: str):
    wait = WebDriverWait(driver, 10)

    wait.until(expected.presence_of_element_located((By.ID, 'usuario')))

    if guardar_capturas:
        guardar_captura(driver, 'login')

    ruc_input = driver.find_element(by=By.ID, value='usuario')
    password_input = driver.find_element(by=By.ID, value='password')
    login_button = driver.find_element(by=By.ID, value='kc-login')

    ruc_input.send_keys(ruc)
    password_input.send_keys(password)

    if guardar_capturas:
        guardar_captura(driver, 'login_con_datos')

    login_button.click()
