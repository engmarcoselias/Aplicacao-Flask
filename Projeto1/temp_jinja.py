from flask import Flask, render_template

app = Flask(__name__)


#--------------VARIAVEIS NO TAMPLATE USANDO JINJA2--------------------------
@app.route('/dados/')
def index():
    z = 2
    y = 3
    x = 5
    return render_template('jinja.html',a=z, b=y, x=x)
#--------------

if __name__ == '__main__':
    app.run(debug=True,port=8000)