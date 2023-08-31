from . import productos
from flask import render_template
from .forms import NewProductForm
import app
import os

#crear rutas del blueprint
@productos.route('/crear', methods= ["GET", "POST"])
def crear():
    p = app.models.Producto()
    form = NewProductForm()
    if form.validate_on_submit():
        #el formulario va a llenar 
        #el nuevo objeto producto
        #automaticamente
        form.populate_obj(p)
        p.imagen = form.imagen.data.filename
        app.db.session.add(p)
        app.db.session.commit()
        #ubicar el archivo imangen en la carpeta app/productos/imagenes
        file = form.imagen.data
        file.save(os.path.abspath(os.getcwd()+ '/app/productos/imagenes/'+ p.imagen))
        return 'produco resgistrado'
    return render_template('new.html' ,form = form)


@productos.route('/listar')
def listar():
    #traer los productos en la base de datos
    productos = app.Producto.query.all()
    #mostrar la vista de listar 
    # enviandole los productos seleccionados por la consulta
    return render_template('listar.html',
                           productos=productos)