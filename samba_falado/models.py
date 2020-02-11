
from samba_falado import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


class Letra(db.Model):
    __tablename__ = 'letra'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    compositores = db.Column(db.String, nullable=False)
    letra = db.Column(db.Text, nullable=False)
    data_envio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __repr__(self):
        return f"Letra('{self.titulo}', '{self.compositores}')"

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    foto = db.Column(db.String, nullable=False, default='default.jpg')
    letras = db.relationship('Letra', backref='enviado por', lazy=True)

    def __repr__(self):
        return f"Usuario('{self.nome}','{self.email}')"


#class Permissoes(db.Model):
    
#class Compositores