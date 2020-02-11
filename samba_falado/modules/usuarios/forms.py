from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from samba_falado.models import Usuario

class Cadastro(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email(),])
    senha = PasswordField('Senha', validators=[DataRequired(), ])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    submit_button = SubmitField('Cadastrar')

    def validate_email(self, email):
        if Usuario.query.filter_by(email=email.data).first():
            print('email já cadastrado')
            raise ValidationError('Email já foi cadastrado. Faça o login!')
            
    

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(),])
    senha = PasswordField('Senha', validators=[DataRequired(), ])
    lembra = BooleanField('Lembrar-me')
    submit_button = SubmitField('Login')