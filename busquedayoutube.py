from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


# URL del video de YouTube
video_url = "https://www.youtube.com/"

# Duración del video en segundos (3 minutos y 3 segundos)
video_duration = 3 * 60 + 6

# Número de veces que queremos que el video se reproduzca
repeat_count = 15

# Iniciar el navegador
driver = webdriver.Chrome()


for _ in range(repeat_count):
    # Acceder al video de YouTube
    driver.get(video_url)

    time.sleep(2)
    
    busqueda= driver.find_element(By.CSS_SELECTOR,"ytd-searchbox")
    busqueda.send_keys("Encontrando los 25 Bugs de Academy Bugs")
    busqueda.send_keys(Keys.ENTER)
    time.sleep(3)
    selecciono=driver.find_element(By.XPATH,"//*[@id='video-title']/yt-formatted-string")
    selecciono.click()
    time.sleep(video_duration)
    #play=driver.find_element(By.CSS_SELECTOR,".ytp-play-button")
    #play.click()
    # Esperar la duración del video
    #time.sleep(video_duration)
    
    # Opcional: Refrescar la página para asegurarse de que el video se reinicia
    # driver.refresh()

# Cerrar el navegador después de la ejecución
driver.quit()
