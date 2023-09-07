from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange

class ProductForm():
     nombre = StringField('ingrese producto:' , 
                         validators=[InputRequired(message="nombre requerido")] )
     precio = IntegerField("ingrese precio:", validators=[
                                                InputRequired(message="precio requerido"),
                                                NumberRange(message="precio fuera de rango",
                                                            min =10000, 
                                                            max =100000)    
                                            ])

class NewProductForm(FlaskForm, ProductForm):
    imagen = FileField(validators=[FileRequired(message="Debe ingresar un archivo"),
                                   FileAllowed(['jpg', 'png'] ,
                                               message="solo se admite imagenes"
                                               ) ],
                        label="Ingrese imagen del producto:")    
    submit = SubmitField("registrar")

class EditProductForm(FlaskForm, ProductForm):
     submit = SubmitField("registrar")