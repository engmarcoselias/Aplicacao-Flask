from flask import Flask,request, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('modelo.html')

@app.route('/loguin',methods=['GET','POST'])
def loguin():
    if request.method == 'POST':
        if request.form['username'] == 'admin'and request.form['pass'] == 'admin':
            return redirect(url_for('sucesso'),code=200)#codigo pra direcionamento automatico é 302
        else:
            abort(401)
    else:
        abort(403)


@app.route('/sucesso')
def sucesso():
    return "Sucesso"


if __name__ == '__main__':
    app.run(debug=True)