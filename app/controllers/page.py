from app import app, db
from flask import render_template, flash, redirect, url_for
from app.model.forms import LoguinForm
from app.model.tables import User
from flask_login import login_user, logout_user

@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return  render_template('index.html', user=user)


#-----------Pagina de loguin-----------------------
@app.route("/loguin", methods=["GET","POST"])
def loguin():
    form = LoguinForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Usuario logado")
            return redirect(url_for("index"))
        else:
            flash("Usuario ou senha incorretos!")
        #print(form.username.data)
        #print(form.password.data)
    return render_template("loguin.html", form=form)


#----------Pagina de Logout----------------------------
@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    flash("Usuario Saiu")
    return redirect(url_for("loguin"))


#FAZENDO CRUD NO BANCO DE DADOS CREATE, READER, UPDATE, DELETE
#@app.route("/crud/<info>")
#@app.route("/crud/", defaults={"info":None})
#def crud(info):
    '''-----------Create----------------------------
    i = User("José", "1234", "marcos@marcos")
    db.session.add(i)
    db.session.commit()
    return "OK"
    ----------------------------------------------'''
    '''-------------Reader---------------------------
    r = User.query.filter_by(username="José").first()
    print(r)
    print(r.username, r.email)
    return "OK"
    ----------------------------------------------'''
    '''-------------Update--------------------------
    r = User.query.filter_by(username="José").first()
    print(r)
    r.username = "Marcos"
    db.session.add(r)
    db.session.commit()
    return "OK"
    ----------------------------------------------'''
    '''----------------Delete------------------------
    r = User.query.filter_by(username="Marcos").first()
    print(r)
    db.session.delete(r)
    db.session.commit()    
    return "OK"
    ----------------------------------------------'''
