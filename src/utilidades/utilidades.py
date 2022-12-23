import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def hover_and_click(driver, button_id):

    hover = ActionChains(driver)

    button = driver.find_element(by=By.ID, value=button_id)
    parent_element = button.find_element(by=By.XPATH, value='./..')

    driver.execute_script("arguments[0].scrollIntoView();", parent_element)
    hover.move_to_element(parent_element).perform()

    driver.execute_script("arguments[0].scrollIntoView();", button)
    hover.move_to_element(button).perform()

    hover.click(button).perform()


def scroll_to_bottom(
    driver,
    element_at_bottom_id='frmFlujoDeclaracion:btnFormularioSiguiente'
):
    element_at_bottom = driver.find_element(
        by=By.ID, value=element_at_bottom_id)
    driver.execute_script("arguments[0].scrollIntoView();", element_at_bottom)
    scroll = ActionChains(driver)
    scroll.move_to_element(element_at_bottom).perform()
    time.sleep(0.5)


def guardar_captura(driver, nombre_archivo):
    driver.save_full_page_screenshot(f"capturas/{nombre_archivo}.png")
