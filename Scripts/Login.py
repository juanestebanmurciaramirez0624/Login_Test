from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
import time

def run_test(driver_path):
    # Configuración de opciones para el navegador
    chrome_options = Options()
    chrome_options.add_argument('--incognito')  # Agregar el modo incógnito

    # Inicializa el servicio de ChromeDriver
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Navega a la página de login
        driver.get('https://apizco.com/mi-cuenta/')

        # Acepta las cookies
        aceptar_cookies = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cky-btn.cky-btn-accept"))
        ).click()

        # Esperar que los elementos en pantalla estén disponibles
        username = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "username"))
        )

        password = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )

        # Limpia y completa los campos de nombre de usuario y contraseña
        username.clear()
        password.clear()
        username.send_keys('Juan_Esteban_Murcia')
        password.send_keys('Saporana0624*')

        # Clic en login
        enviar_login = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.NAME, "login"))
        ).click()

        # Manejar la alerta automáticamente (si aparece después de enviar el formulario)
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()  # Aceptar alerta
            print("Alerta cerrada automáticamente")
        except NoAlertPresentException:
            print("No se encontró ninguna alerta después de enviar el formulario")

    finally:
        # Cierra el navegador
        time.sleep(10)
        driver.quit()