from record_screen import record_screen
from Login import run_test
# Inicia la grabación en un hilo o proceso separado
import threading

def main():
    # Parámetros para la grabación y el test
    video_file = 'test_recording.mp4'
    recording_duration = 60  # Duración de la grabación (en segundos) para cubrir el test
    driver_path = r'C:\Users\Juan Esteban\Documents\Automatización_Casos_de_prueba\chromedriver-win64\chromedriver.exe'

    def start_recording():
        record_screen(video_file=video_file, recording_duration=recording_duration)

    # Inicia la grabación
    recording_thread = threading.Thread(target=start_recording)
    recording_thread.start()

    # Ejecuta el test
    run_test(driver_path=driver_path)

    # Espera que la grabación termine
    recording_thread.join()

if __name__ == "__main__":
    main()