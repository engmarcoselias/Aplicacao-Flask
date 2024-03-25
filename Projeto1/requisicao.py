from flask import Flask, request, render_template

app = Flask(__name__)

#----------------Objetos de requisição HTTP------------------

@app.route('/')
def index():
    print(request.method, request.args)
    return

if __name__ == '__main__':
    app.run(debug=True)
