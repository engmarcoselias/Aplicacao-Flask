from flask import Flask,render_template


app = Flask(__name__)
app.secret_key = 'flask'


@app.route("/form")
def form():
    return render_template("form.html", titulo='Test Asp')



if __name__== '__main__':
    app.run(port=5000)