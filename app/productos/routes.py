from . import productos
from flask import render_template, redirect, flash 
from .forms import NewProductForm, EditProductForm
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
        flash("Producto registrado con exito")
        return redirect('/productos/listar')
    return render_template('new.html' ,form = form)

@productos.route('/listar')
def listar():
    #traer los productos en la base de datos
    productos = app.Producto.query.all()
    #mostrar la vista de listar 
    # enviandole los productos seleccionados por la consulta
    return render_template('listar.html',
                           productos=productos)

@productos.route('/editar/<producto_id>', 
                 methods=['GET', 'POST'])
def editar(producto_id):
    #seleccionar el producto con el id
    p = app.models.Producto.query.get(producto_id)
    #cargo el formulario con los atibutos del producto
    form_edit = EditProductForm(obj = p)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Producto editado exitosamente")
        return redirect("/productos/listar")
    return render_template('new.html', 
                    form = form_edit)

@productos.route('/eliminar/<producto_id>',
                 methods=['GET', 'POST'])
def eliminar(producto_id):
    #Seleccionar el producto a eliminar
    p = app.models.Producto.query.get(producto_id)
    #Eliminar el producto
    app.db.session.delete(p)
    app.db.session.commit()
    flash("Producto eliminado exitosamente")
    return redirect("/productos/listar")
