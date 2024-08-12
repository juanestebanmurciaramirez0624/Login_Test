import time
import mss
import cv2
import numpy as np

def start_recording(filename='test_login.mp4', codec='mp4v'):
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}  # Define el tamaño del monitor
    fourcc = cv2.VideoWriter_fourcc(*codec)  # Define el códec de video
    out = cv2.VideoWriter(filename, fourcc, 20.0, (monitor["width"], monitor["height"]))
    return out, monitor

def stop_recording(out):
    out.release()  # Libera el objeto VideoWriter

def record_screen(video_file='test_login.mp4', recording_duration=1):
    out, monitor = start_recording(filename=video_file)
    start_time = time.time()


    with mss.mss() as sct:
        while True:
            # Captura la pantalla
            img = sct.grab(monitor)
            frame = np.array(img)  # Convierte la imagen a un array de NumPy
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Convierte el color de BGRA a BGR
            out.write(frame)  # Escribe el frame en el archivo de video

            # Detén la grabación después del tiempo especificado
            if time.time() - start_time > recording_duration:
                break

    stop_recording(out)