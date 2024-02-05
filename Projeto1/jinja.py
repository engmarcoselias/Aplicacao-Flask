from flask import Flask,render_template, request
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nossa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica


app = Flask(__name__)
app.secret_key = 'flask'


#------------------Criando rota-------------------------------------------
@app.route("/")
def index():
    return "Hello Word"

#--------------------Renderizar template----------------------------------
@app.route("/form/")
def form():
    return render_template("form.html")

#-------------------Acessar o valor de um parâmetro de URL-----------------

@app.route("/param")
def param():
    name = request.args.get('name')
    return "Hello, {}!".format(name)

#---------------------Exemplo de requisição calculadora--------------------

@app.route('/cal')
def cal():
   
  
  a = request.args.get('a') 
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



if __name__== '__main__':
    app.run(port=5000)