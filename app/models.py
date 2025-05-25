from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)
    @property
    def password(self):
        raise AttributeError('Password is not readable')
    
    @password.setter
    def password(self, plaintext_password):
        self.password_hash = generate_password_hash(plaintext_password)

    def __repr__(self):
        return f'<User {self.username}>'