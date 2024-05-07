from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, nome, password):
        self.nome = nome
        self.password = password

@app.route('/')
def inicio():
    usuario = Usuario.query.all()
    return render_template('inicio.html', usuario=usuario)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        usuario = Usuario(request.form['nome'], request.form['password'])
        db.session.add(usuario) # adicionando usuario ao banco de dados
        db.session.commit()# commite para confirmar processo ao banco de dados
        return redirect(url_for('inicio'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    
    return redirect(url_for('inicio'))




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)