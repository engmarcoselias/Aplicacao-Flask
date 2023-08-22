import os.path
basedir = os.path.abspath(os.path.dirname(__file__))#adicionar o banco de dados na rais do projeto

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'app.db')

SECRET_KEY = 'chave-secreta-form'