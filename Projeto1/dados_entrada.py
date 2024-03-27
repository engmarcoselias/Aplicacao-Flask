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
    request_data = request.get_json()

    '''Se o objeto JSON enviado com a solicitação não tiver uma chave que seja acessada na sua função de visualização, então a solicitação falhará. Se não quiser que ela falhe quando uma chave não existir, será necessário verificar se a chave existe antes de tentar acessá-la.'''

    language = None
    framework = None
    python_version = None
    example_test = None
    boolean_test = None

#Verificação se a chave existe
    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']            
    
    language = request_data['language']
    framework = request_data['framework']

    #duas keys são por conta do objeto aninhado
    python_version = request_data['version_info']['flask']

    #um indice e necessario por conta do array
    example_test = request_data['examples'][0]

    boolean_test = request_data['boolean_test']

    return '''
            The language value is: {}
            The framework value is:{}
            The Python version is:{}
            The item at index 0 the example list is: {}
            The boolean value is: {}'''.format(language, framework, python_version, example_test, boolean_test)


if __name__ == '__main__':
    app.run(debug=True, port=5000)