from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crear la instancia de SQLAlchemy sin pasar app
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Cargar la configuración desde el archivo config
    app.config.from_object('config.DevelopmentConfig')

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    # Importar y registrar blueprints
    from MyBlog.views.auth import auth
    app.register_blueprint(auth)
    
    from MyBlog.views.blog import blog
    app.register_blueprint(blog)

    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()
        
    return app
