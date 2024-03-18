from flask import Flask,request, render_template, redirect, url_for


#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nossa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica


app = Flask(__name__)


#------------------Criando rota-------------------------------------------
@app.route("/")
def index():
    return render_template('index.html')

#--------------------Renderizar template----------------------------------
@app.route("/form/")
def form():
    return render_template("form.html")

#-------------------Acessar o valor de um parâmetro de URL-----------------

@app.route("/param/<nome>")
def param(nome):
    name = request.args.get('name')
    return "Hello, {}!".format(name)

#--------------------------------URL dinamica------------------------------
#Exemplo 1 com nome
@app.route("/dinamica/<name>")
def dinamica_nome(name):
    return "<p>Ola {}</p>".format(name)

#Exemplo 2 com valor numerico
@app.route("/num/<int:numerico>")
def dinamica_num(numerico):
    return "<p>Valor inteiro {}</p>".format(numerico)

#Exemplo 3 com flout
@app.route("/float/<float:flt>")
def dinamica_float(flt):
    return "<p>Float {}</p>".format(flt)

#----------------------------------Redirecionamento----------------------------------------
@app.route("/redir")#CRIANDO A ROTA ADMIN
def redir():
    return "<h1>Admin</h>"

@app.route("/guest/<name1>")#CRIANDO A ROTA GUEST
def guest(name1):
    return "<h1>Usuario {}</h>".format(name1)

@app.route("/user/<name1>")#CRIANDO DIRECIONAMENTO DEPENDNDO DO VALOR DE ENTRADA
def user(name1):
    if name1 == "admin":
        return redirect(url_for('redir'))
    else:
        return redirect(url_for('guest',name1=name1))

#--------------------------------------Arquivos Estaticos-----------------------------------
@app.route("/static")
def arq_static():
    return render_template('static.html')

#--------------------------------------Métodos HTTP-----------------------------------------
#CONNECT
#DELETE
#GET
#HEAD
#OPTIONS
#PATH
#POST
#PUT
#TRACE


'''
#---------------------Exemplo de requisição calculadora--------------------

@app.route('/cal')
def cal():
   
  
  a = request.args.get('a') #request.arg pega o valor adcionado na url
  b = request.args.get('b') 
  operator = request.args.get('operator')
 
  if a and b and operator:
    a = int(a)
    b = int(b)
 
    if operator == 'add':
      result = a + b
    elif operator == 'subtract':
      result = a - b
    elif operator == 'multiply':
      result = a * b
    elif operator == 'divide':
      result = a / b
 
    return f'{a} {operator} {b} = {result}'
  else:
    return 'Error: Insufficient arguments'
  #---------------------------------------------------------------------------------
'''

if __name__== '__main__':
    app.run(port=5000, host='localhost', debug=True)# debug quando esta em True mostra traceback da aplicação