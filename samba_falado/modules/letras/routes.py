from flask import Blueprint
from flask import render_template, redirect, url_for, flash
from samba_falado.modules.letras.forms import EnviarLetra
from flask_login import login_required, current_user
from samba_falado.models import Letra
from samba_falado import db


letras = Blueprint('letras', __name__)


@letras.route('/enviarLetra', methods=['GET', 'POST'])
@login_required
def enviarLetra():
    form = EnviarLetra()
    if form.validate_on_submit():
        nova_letra = Letra(titulo=form.titulo.data, compositores=form.compositores.data, letra=form.letra.data, user_id=current_user.id)
        db.session.add(nova_letra)
        db.session.commit()
        flash('Letra enviada com!')
        print('Letra enviada com!')
        #return redirect(url_for('letras.enviarLetra'))
    return render_template('letras/enviarLetra.html', form=form)


