from flask import Flask,render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['GET','POST'])
def setcookie():
    if request.method == 'POST':
        dados = request.form['c']
        resp = make_response(render_template('setcookie.html'))
        resp.set_cookie('testcookie', dados)
    return resp

@app.route('/getcookie')
def getcookie():
    cookiename = request.cookies.get('testcookie')
    print(cookiename)
    return '<h1>Valor cookie é: {}</h1>'.format(cookiename)



if __name__ == '__main__':
    app.run(debug=True)