from flask import Flask, render_template

app = Flask(__name__)

@app.route('/base')
def heranca():
    return render_template('pagina_base.html')

@app.route('/heranca')
def heranca1():
    return render_template('pagina_heranca.html')


if __name__ == '__main__':
    app.run(debug=True)