from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL del video de YouTube
video_url = "https://youtu.be/dJOMbnyzNNU?si=A0MkaWk547qMSfvY"

# Duración del video en segundos (3 minutos y 3 segundos)
video_duration = 5 * 60 + 28

# Número de veces que queremos que el video se reproduzca
repeat_count = 9

# Iniciar el navegador
driver = webdriver.Chrome()


for _ in range(repeat_count):
    # Acceder al video de YouTube
    driver.get(video_url)

    time.sleep(2)

    play=driver.find_element(By.CSS_SELECTOR,".ytp-play-button")
    play.click()
    # Esperar la duración del video
    time.sleep(video_duration)
    
    # Opcional: Refrescar la página para asegurarse de que el video se reinicia
    # driver.refresh()

# Cerrar el navegador después de la ejecución
driver.quit()
