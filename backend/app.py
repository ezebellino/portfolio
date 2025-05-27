# backend/app.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from routes.projects import projects_bp
import os

# Configuración global de la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'portfolio.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db = SQLAlchemy(app)

# Importar modelos después de inicializar db
from models.project import Project

# Crear tablas si no existen
with app.app_context():
    db.create_all()

# Registrar rutas
app.register_blueprint(projects_bp)

if __name__ == "__main__":
    app.run(debug=True)


