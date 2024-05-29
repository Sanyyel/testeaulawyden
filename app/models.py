from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return user.query.get(user_id)

class user(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
class hotel(db.Model):
    __tablename__ = "hotels"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    local = db.Column(db.String(255), nullable=True)
    preco = db.Column(db.Integer, nullable = True)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class domicilio(db.Model):
    __tablename__ = "domicilios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    endereco = db.Column(db.String(255), nullable=True)
    precocom = db.Column(db.Integer, nullable=True)
    precoalu = db.Column(db.Integer, nullable=True)
    dimens = db.Column(db.String(255), nullable=True)
    qtdcomodos= db.Column(db.Integer, nullable=True)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


   

   