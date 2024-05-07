from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOUDER_FOLDER = os.path.join(os.getcwd(),'upload')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload')
def upload():
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
