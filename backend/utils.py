import sounddevice as sd
from scipy.io.wavfile import write
import os
import whisper

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
    
def transcribe_audio(audio_path, output_folder):
    """
    Transcreve o áudio usando o Whisper e salva a transcrição em um arquivo .txt.
    """
    try:
        # Verifica se o arquivo de áudio existe
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")

        # Carrega o modelo Whisper
        model = whisper.load_model("base")
        print("Modelo Whisper carregado.")

        # Realiza a transcrição
        result = model.transcribe(audio_path)
        transcription = result['text']
        print(f"Transcrição realizada: {transcription}")

        # Caminho do arquivo de transcrição
        transcription_path = os.path.join(output_folder, 'transcription.txt')

        # Salva a transcrição em um arquivo .txt
        with open(transcription_path, 'w', encoding='utf-8') as f:
            f.write(transcription)

        print(f"Transcrição salva em: {transcription_path}")
        return transcription_path
    except Exception as e:
        print(f"Erro ao transcrever áudio: {e}")
        return None