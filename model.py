from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserHW3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)

    def __repr__(self):
        return f'id{self.user_id}({self.firstname, self.lastname, self.email})'
