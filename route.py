from flask import Flask, render_template, request, flash, redirect
from forms import ContactForm
from flask.ext.mail import Message, Mail# Mail: realiza la conexion con Google/ Message: es el encargado de armar el mensaje.
from flask_bootstrap import Bootstrap
import time


app = Flask(__name__)      
Bootstrap(app)

mail = Mail()

app.secret_key = 'somesecret!'
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'somesecret@gmail.com'
app.config["MAIL_PASSWORD"] = 'somesecret'


mail.init_app(app)
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/family', methods=['GET', 'POST'])
def family():
  form = ContactForm()

  if request.method == 'POST':
  	 if form.validate() == False:
  	 	flash('Algunos campos son requeridos.')
  	 	print "Post NOT validate!"
  	 	return render_template('family.html', form=form) 
  	 else:
  	 	selected_options = request.form.getlist("check")
  	 	selected_country = request.form.getlist("country")
  		msg = Message("Me interesa!", sender='unclegeorge2k@gmail.com', recipients=['unclegeorge2k@gmail.com'])
  		msg.body = """Nombre: %s, Email:%s, Pais: %s, Opciones: %s """ % (form.name.data, form.email.data, selected_country, selected_options)
  		mail.send(msg)
		return render_template('gracias-es.html')
    #return render_template('gracias-es.html')
  elif request.method == 'GET':
      return render_template('family.html', form=form)

@app.route('/thankes')
def thankses():
  render_template('gracias-es.html')
  #time.sleep(5)
  return render_template('gracias-es.html')

@app.route('/nanny', methods=['GET', 'POST'])
def nanny_es():
  form = ContactForm()

  if request.method == 'POST':
     if form.validate() == False:
        flash('Algunos campos son requeridos.')
        print "Post NOT validate!"
        return render_template('nanny.html', form=form) 
     else:
        selected_options = request.form.getlist("check")
        selected_country = request.form.getlist("country")
        msg = Message("TRABAJAR Me interesa!", sender='unclegeorge2k@gmail.com', recipients=['unclegeorge2k@gmail.com'])
        msg.body = """Nombre: %s, Email:%s, Pais: %s, Opciones: %s """ % (form.name.data, form.email.data, selected_country, selected_options)
        mail.send(msg)
        return render_template('gracias-es.html')
  elif request.method == 'GET':
       return render_template('nanny.html', form=form)

  #return render_template('gracias-es.html')



####################### Logica en ingles #####################
@app.route('/en')
def home_en():
  return render_template('home-en.html')

@app.route('/family_en', methods=['GET', 'POST'])
def family_en():
  form = ContactForm()

  if request.method == 'POST':
     if form.validate() == False:
      flash('Some fields are requeried.')
      print "Post NOT validate!"
      return render_template('family-en.html', form=form) 
     else:
      selected_options = request.form.getlist("check")
      selected_country = request.form.getlist("country")
      msg = Message("Me interesa!", sender='unclegeorge2k@gmail.com', recipients=['unclegeorge2k@gmail.com'])
      msg.body = """Nombre: %s, Email:%s, Pais: %s, Opciones: %s """ % (form.name.data, form.email.data, selected_country, selected_options)
      mail.send(msg)
     return render_template('gracias-en.html')
  elif request.method == 'GET':
      return render_template('family-en.html', form=form)

####################### Logica en portugues #####################

@app.route('/br')
def home_br():
  return render_template('home-br.html')
 
@app.route('/family_br', methods=['GET', 'POST'])
def family_br():
  form = ContactForm()

  if request.method == 'POST':
     if form.validate() == False:
      flash('Some fields are requeried.')
      print "Post NOT validate!"
      return render_template('family-br.html', form=form) 
     else:
      selected_options = request.form.getlist("check")
      selected_country = request.form.getlist("country")
      msg = Message("Me interesa!", sender='unclegeorge2k@gmail.com', recipients=['unclegeorge2k@gmail.com'])
      msg.body = """Nombre: %s, Email:%s, Pais: %s, Opciones: %s """ % (form.name.data, form.email.data, selected_country, selected_options)
      mail.send(msg)
     return render_template('gracias-br.html')
  elif request.method == 'GET':
      return render_template('family-br.html', form=form)

if __name__ == '__main__': # Esto es una convencion para asegurar que la app solo correra cuando se ejecute app.py?!?! learning flask framework pag 29
  app.run(debug=True)
