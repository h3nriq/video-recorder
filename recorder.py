import cv2
import keyboard
import pyautogui
import numpy as np
import os

# Definindo o FPS do vídeo
fps = 30

# Definindo o nome do video
video_name = "video.avi"

# Verificar se o arquivo já existe, em caso afirmativo, renomeia
base_name, extension = os.path.splitext(video_name)
counter = 1

while os.path.exists(video_name):
    video_name = f"{base_name}-{counter}{extension}"
    counter += 1

# Pegando o tamanho da tela do seu computador
screen_size = tuple(pyautogui.size())

# Setando o codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Criando o vídeo
video = cv2.VideoWriter(video_name, codec, fps, screen_size)

while True:
    frame = pyautogui.screenshot()

    # Convertendo o objeto em matriz
    matrices_frame = np.array(frame)

    # Convertendo cor para o padrão do cv2 - BGR
    convert_color_frame = cv2.cvtColor(matrices_frame, cv2.COLOR_RGB2BGR)

    # Salvando o frame tirado
    video.write(convert_color_frame)

    # Parando a captura de video ao clicar a tecla Enter
    if keyboard.is_pressed("esc"):
        break

# Publicando o video final
video.release()

# Garantindo que o cv2 pare de rodar
cv2.destroyAllWindows()
