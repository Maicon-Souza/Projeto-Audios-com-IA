import sounddevice as sd
from scipy.io.wavfile import write
import os

def capture_audio(upload_folder, duration=5, sample_rate=16000):
    """
    Captura áudio do microfone e salva em um arquivo.
    """
    try:
        print("Gravando... Fale agora!")
        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Espera até a gravação terminar

        # Caminho do arquivo
        file_path = os.path.join(upload_folder, 'captured_audio.wav')
    
        # Salva o áudio em um arquivo
        write(file_path, sample_rate, audio)
        print(f"Áudio capturado e salvo em: {file_path}")

        return file_path
    except Exception as e:
        print(f"Erro ao capturar áudio: {e}")
        return None
