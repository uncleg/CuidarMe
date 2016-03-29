from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField, validators, ValidationError, SelectField

class ContactForm(Form):
  name = TextField("Nombre/Name/Nome")
  email = TextField("Email",  [validators.Required("Insert an email / Ingrese su email"), validators.Email("Insert a valid  email / Ingrese un email valido")])
  submit = SubmitField("Send")