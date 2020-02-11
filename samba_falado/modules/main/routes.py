
from flask import Blueprint, render_template
from samba_falado.models import Letra, Usuario

main = Blueprint('main', __name__)


@main.route('/home')
@main.route('/')
def home():
    letras = Letra.query.order_by(Letra.data_envio.desc()).all()
    return render_template('main/home.html', letras=letras)


@main.route('/about')
@main.route('/sobre')
def sobre():
    
    return render_template('main/sobre.html')