from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL del video de YouTube
video_url = "https://www.youtube.com/watch?v=quKMb0yVWwk"

# Duración del video en segundos (3 minutos y 3 segundos)
video_duration = 2 * 60 + 10

# Número de veces que queremos que el video se reproduzca
repeat_count = 10

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
