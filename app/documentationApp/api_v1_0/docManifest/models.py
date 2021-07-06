from app.db import db, BaseModelMixin

class Manifest(db.Model,BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.username

    def __str__(self):
        return f'{self.username}'