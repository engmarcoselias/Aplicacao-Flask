from flask import Flask, request

app = Flask(__name__)


#--------------------------Usando strings de consulta----------------------------------------------

@app.route('/query-example')
def query_example():

    #Se a chave de linguagem não existir retorna None
    language = request.args.get('language')
    
    #se a chave de linguagem não existir retorna erro 400, bad request error
    framework = request.args['framework']

    #se a chave de linguagem não existir retorna None
    website = request.args.get('website')

    return '''
                <h1>The language value is: {}</h1>
                <h1>The language value is: {}</h1>
                <h1>The language value is: {}</h1>'''.format(language, framework, website)
    

#-------------------------Usando dados de formulario------------------------------------------

@app.route('/form-example',methods=['GET','POST'])#modificando a rota para aceitar solicitações GET e POST
def form_example():
    if request.method =='POST':
        language = request.form.get('language')#O Request.Form é usado para obter informações de um submit de um formulário HTML que foi enviado via POST. Como a informação do POST é invisível ao usuário, você deve recuperar através do método Request.
        framework = request.form.get('framework')
        return '''
                <h1>The language value is: {}</h1>
                <h1>The framework value is: {}</h1>'''.format(language, framework)

            
    return '''
            <form method="POST">
            <div><label>Language: <input type="text" name="language"></label></div>
            <div><label>Framework: <input type="text" name="framework"></label></div>
            <input type="submit" valeu="Submit">
            </form>'''

#-------------------------------------Usando dados JSON----------------------------------------

@app.route('/json-example',methods=['POST'])
def json_example():
    return 'JSON Object Example'


if __name__ == '__main__':
    app.run(debug=True, port=5000)