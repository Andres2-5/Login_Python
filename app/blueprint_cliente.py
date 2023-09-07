from flask import Blueprint

#crear y configurar el blueprint
blueprint_cliente = Blueprint('blueprint_cliente',
                         __name__,
                         url_prefix = '/cliente' )

#crear ruta del blueprint
@blueprint_cliente.route('/saludo')
def saludo():
    return 'pepe'