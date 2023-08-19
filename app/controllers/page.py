from app import app
from flask import render_template


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return  render_template('index.html', user=user)

@app.route("/loguin")
def loguin():
    return render_template("loguin.html")