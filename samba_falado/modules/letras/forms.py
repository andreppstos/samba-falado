from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class EnviarLetra(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired(),])
    compositores = StringField('Compositores', validators=[DataRequired(), ])
    letra = TextAreaField('Letra', validators=[DataRequired(),])
    submit_button = SubmitField('Enviar')
