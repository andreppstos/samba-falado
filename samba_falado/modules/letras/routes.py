from flask import Blueprint
from flask import render_template, redirect, url_for, flash, abort, request
from samba_falado.modules.letras.forms import EnviarLetra
from flask_login import login_required, current_user
from samba_falado.models import Letra
from samba_falado import db


letras = Blueprint('letras', __name__)


@letras.route('/letras/enviar', methods=['GET', 'POST'])
@login_required
def enviar():
    form = EnviarLetra()
    if form.validate_on_submit():
        nova_letra = Letra(titulo=form.titulo.data, compositores=form.compositores.data, 
        letra=form.letra.data, autor=current_user)
        db.session.add(nova_letra)
        db.session.commit()
        flash('Letra enviada com!')
        print('Letra enviada com!')
        return redirect(url_for('main.home'))
    return render_template('letras/enviar-editar.html', form=form, legend='Enviar Letra')


@letras.route('/letra/<int:letra_id>')
def letra(letra_id):
    letra = Letra.query.get_or_404(letra_id)
    return render_template('letras/letra.html', letra=letra)


@letras.route('/letra/<int:letra_id>/editar', methods=['GET', 'POST'])
@login_required
def editar(letra_id):
    letra = Letra.query.get_or_404(letra_id)
    if letra.autor != current_user:
        abort(403)
    form = EnviarLetra()
    if form.validate_on_submit():
        letra.titulo = form.titulo.data
        letra.compositores = form.compositores.data
        letra.letra = form.letra.data
        db.session.commit()
        flash('Letra foi editada')
        print('Letra foi editada')
        return redirect(url_for('letras.letra', letra_id=letra.id))
    elif request.method == 'GET':
        form.titulo.data =  letra.titulo
        form.compositores.data = letra.compositores
        form.letra.data = letra.letra
    return render_template('letras/enviar-editar.html', form=form, legend='Editar Letra')


@letras.route('/letra/<int:letra_id>/excluir')
@login_required
def excluir(letra_id):
    letra = Letra.query.get_or_404(letra_id)
    if letra.autor != current_user:
        abort(403)
    db.session.delete(letra)
    db.session.commit()
    flash('A letra foi excluida')
    print('A letra foi excluida')
    return redirect(url_for('main.home'))