from flask import Flask

app = Flask(__name__, static_folder='Projeto1/static')


if __name__ == ('__main__'):
    app.run(debug=True, port=8000)