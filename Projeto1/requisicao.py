from flask import Flask, request, render_template
import json

app = Flask(__name__)

#----------------Objetos de requisição HTTP------------------

@app.route('/', methods=['GET','POST'])
def index():
    print(request.method, request.args)
    return json.dumps(request.args['idade'])#transforma os dados recebdos em json
    

if __name__ == '__main__':
    app.run(debug=True)
