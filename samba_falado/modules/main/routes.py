
from flask import Blueprint, render_template
from samba_falado.models import Letra, Usuario

main = Blueprint('main', __name__)


@main.route('/home')
@main.route('/')
def index():
    letras = Letra.query.all()
    autor = Usuario.query.all()
    return render_template('main/index.html', letras=letras, autor=autor)


@main.route('/about')
@main.route('/sobre')
def sobre():
    
    return render_template('main/sobre.html')