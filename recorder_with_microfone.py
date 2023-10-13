import cv2
import numpy as np
import pyautogui
import pyaudio
import wave
import threading
import os

# Função para renomear arquivos caso já existam na pasta 
def verify_name_file(name_file):
    base_name, extension = os.path.splitext(name_file)
    counter = 1

    while os.path.exists(name_file):
        name_file = f"{base_name}_{counter}{extension}"
        counter += 1

    return name_file

# Configurando recording 
is_recording = True

# Configurando nomes de arquivo de audio e video default
df_video_name = "video.avi"
df_audio_name = "audio.wav"

# Configurando vídeo
screen_size = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 20.0
filename_video = verify_name_file(df_video_name)
out = cv2.VideoWriter(filename_video, fourcc, fps, screen_size)

# Configurando audio
filename_audio = verify_name_file(df_audio_name)
chunk = 1024
sample_format = pyaudio.paInt16
channels = 2 # Estério 
fs = 44100  # Sample rate

p = pyaudio.PyAudio()
stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []

# Função para capturar vídeo
def capture_video():
    while is_recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

# Função para capturar áudio
def capture_audio():
    while is_recording:
        data = stream.read(chunk)
        frames.append(data)

# Começar a gravar
video_thread = threading.Thread(target=capture_video)
audio_thread = threading.Thread(target=capture_audio)
video_thread.start()
audio_thread.start()

# Para parar a gravação, pressione 'q'
key = input("Press q to stop: ")
if key == 'q':

    # Finalizar whiles de áudio e vídeo
    is_recording = False
    
    # Finalizar a gravação de vídeo
    out.release()
    cv2.destroyAllWindows()
    
    # Finalizar a gravação de áudio
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(filename_audio, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()