from app import app
from flask import render_template
from app.model.forms import LoguinForm

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