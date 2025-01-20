from flask import Blueprint, jsonify, current_app
from .utils import capture_audio, transcribe_audio
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return jsonify({"message": "API de Captura de Áudio funcionando!"})

@bp.route('/capture-audio', methods=['GET'])
def capture_audio_route():
    """
    Endpoint para capturar áudio do microfone.
    """
    file_path = capture_audio(current_app.config['UPLOAD_FOLDER'], duration=5)
    if file_path:
        return jsonify({"message": "Áudio capturado com sucesso!", "file_path": file_path})
    else:
        return jsonify({"error": "Falha ao capturar o áudio!"}), 500