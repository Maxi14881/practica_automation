from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()

driver.get("https://www.saucedemo.com/v1/")  # Cargo en el navegador


time.sleep(3)

txt_usuario = driver.find_element(By.ID,"user-nam")
txt_usuario.send_keys("standard_user")

txt_clave = driver.find_element(By.ID,"password")
txt_clave.send_keys("secret_sauce")

btn_login= driver.find_element(By.ID,"login-button").click()

titulo=driver.find_element(By.CSS_SELECTOR,"#inventory_filter_container > div")

if titulo.text == "Product" :
    print("Test correcto")
else:
    print("Error")
    exit()

# Cerrar el navegador 1
driver.quit()
