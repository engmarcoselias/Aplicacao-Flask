from app import app, db
from flask import render_template
from app.model.forms import LoguinForm
from app.model.tables import User

@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return  render_template('index.html', user=user)

@app.route("/loguin", methods=["GET","POST"])
def loguin():
    form = LoguinForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template("loguin.html", form=form)


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
