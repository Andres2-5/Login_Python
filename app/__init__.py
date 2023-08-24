from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config 
from .mi_blueprint import mi_blueprint
from app.productos import productos
import pymysql
pymysql.install_as_MySQLdb()
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
