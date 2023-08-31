from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config 
from .mi_blueprint import mi_blueprint
from app.productos import productos

from flask_bootstrap import Bootstrap



#Creacion y configuracion
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

#registro de blueprints
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)

#Crear objetos de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, 
                  db)

from .models import Producto, Cliente, Detalle,Venta

@app.route('/prueba')
def prueba():
    return render_template("prueba.html")