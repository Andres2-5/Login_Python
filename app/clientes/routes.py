from . import clientes
from flask import render_template, redirect, flash 
from .forms import NewClientForm, EditClientForm
import app
import os

#crear rutas del blueprint
@clientes.route('/crear', methods= ["GET", "POST"])
def crear():
    c = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        #el formulario va a llenar 
        #el nuevo objeto producto
        #automaticamente
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        flash("Cliente registrado con exito")
        return redirect('/clientes/listar')
    return render_template('new.html' ,form = form)

@clientes.route('/listar')
def listar():
    #traer los productos en la base de datos
    clientes = app.Cliente.query.all()
    #mostrar la vista de listar 
    # enviandole los productos seleccionados por la consulta
    ##return "hola"
    ##return clientes.username
    return render_template('listarclientes.html',
                           clientes=clientes)

@clientes.route('/editar/<cliente_id>', 
                 methods=['GET', 'POST'])
def editar(cliente_id):
    #seleccionar el producto con el id
    c = app.models.Cliente.query.get(cliente_id)
    #cargo el formulario con los atibutos del producto
    form_edit = EditClientForm(obj = c)
    if form_edit.validate_on_submit():
        form_edit.populate_obj(c)
        app.db.session.commit()
        flash("Cliente editado exitosamente")
        return redirect("/clientes/listar")
    return render_template('newclientes.html', 
                    form = form_edit)

@clientes.route('/eliminar/<cliente_id>',
                 methods=['GET', 'POST'])
def eliminar(cliente_id):
    #Seleccionar el producto a eliminar
    c = app.models.Cliente.query.get(cliente_id)
    #Eliminar el producto
    app.db.session.delete(c)
    app.db.session.commit()
    flash("Cliente eliminado exitosamente")
    return redirect("/clientes/listar")
