from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Configurações do aplicativo
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Registrar rotas
    from .routes import bp as main_routes
    app.register_blueprint(main_routes)

    return app
