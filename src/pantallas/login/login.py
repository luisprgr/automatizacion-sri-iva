from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.common.by import By

from src.utilidades.utilidades import guardar_captura
from src.pantallas.login.ids import (
    INPUT_USER_ID,
    INPUT_PASSWORD_ID,
    BUTTON_LOGIN_ID
)


def login_sri(driver, guardar_capturas: bool, ruc: str, password: str):
    wait = WebDriverWait(driver, 10)

    wait.until(expected.presence_of_element_located((By.ID, INPUT_USER_ID)))

    if guardar_capturas:
        guardar_captura(driver, 'login')

    ruc_input = driver.find_element(by=By.ID, value=INPUT_USER_ID)
    password_input = driver.find_element(by=By.ID, value=INPUT_PASSWORD_ID)
    login_button = driver.find_element(by=By.ID, value=BUTTON_LOGIN_ID)

    ruc_input.send_keys(ruc)
    password_input.send_keys(password)

    if guardar_capturas:
        guardar_captura(driver, 'login_con_datos')

    login_button.click()
