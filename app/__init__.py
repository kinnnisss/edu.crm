from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    """Application Factory"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'cle-par-defaut')
    app.config['APP_NAME'] = os.getenv('APP_NAME', 'ScolarISM')

    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    # Route de test pour la racine
    @app.route('/')
    def index():
        return f"<h1>Bienvenue sur ScolarISM </h1><p><a href='/auth/login'>Se connecter</a></p>"
    
    return app