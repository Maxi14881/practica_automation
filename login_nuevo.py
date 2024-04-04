from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# Iniciar el navegador
driver = webdriver.Chrome()

# Abrir la página web
driver.get("https://www.saucedemo.com/v1/")

# Esperar 3 segundos para que la página cargue completamente
time.sleep(3)

# Ingresar el usuario y la contraseña
txt_usuario = driver.find_element(By.ID, "user-name")
txt_usuario.send_keys("standard_user")

txt_clave = driver.find_element(By.ID, "pasword")
txt_clave.send_keys("secret_sauce")

# Hacer clic en el botón de login
btn_login = driver.find_element(By.ID, "login-button").click()

# Esperar 3 segundos más para que la página cargue completamente
time.sleep(3)

# Verificar si el título es "Products"
titulo = driver.find_element(By.CSS_SELECTOR, "#inventory_filter_container > div")

if titulo.text == "Products":
    print("Test correcto")
    # Obtener la fecha y hora actual
    now = datetime.datetime.now()
    # Crear el nombre del archivo con la fecha y hora actual
    nombre_archivo = f"resultado_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    # Escribir "ok" y la fecha y hora en el archivo
    with open(nombre_archivo, "w") as archivo:
        archivo.write("ok\n")
        archivo.write(now.strftime("%Y-%m-%d %H:%M:%S"))
else:
    print("Error")
    exit()

# Cerrar el navegador
driver.quit()
