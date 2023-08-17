from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String)


    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
