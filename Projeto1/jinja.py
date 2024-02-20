from flask import Flask, render_template, request

app = Flask(__name__)


#--------------VARIAVEIS NO TAMPLATE USANDO JINJA2--------------------------
@app.route('/dados/')
def index():
    z = 2
    y = 3
    x = 5
    return render_template('jinja.html',a=z, b=y, x=x)
#----------------------------------------------------------------------------
#--------------USANDO FOR EXEMPLO------------------------------------------------
@app.route('/tabela')
def tabela():
    a = 0
    b = 0
    x = 0
    query = request.args.to_dict()
    return render_template('jinja.html',a=a,b=b,x=x,query=query)

if __name__ == '__main__':
    app.run(debug=True,port=8000)