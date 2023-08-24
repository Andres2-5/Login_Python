from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NewProductForm(FlaskForm):
    nombre = StringField('ingrese producto:')
    precio = StringField("ingrese precio:")
    submit = SubmitField("registrar:")