from flask import  Blueprint
from flask import render_template, redirect, url_for, flash, request
from samba_falado.modules.usuarios.forms import Login, Cadastro
from samba_falado.models import Letra, Usuario
from samba_falado import db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required


usuarios = Blueprint('usuarios', __name__)


@usuarios.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Cadastro()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        novo_usuario = Usuario(nome=form.nome.data, email=form.email.data, senha=hashed_pw)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastrado com sucesso!')
        print('Cadastrado com sucesso!')
        return redirect(url_for('usuarios.login'))
    else:
        return render_template('usuarios/cadastro.html', form=form)


@usuarios.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Login()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(email=form.email.data).first() 
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user, remember=form.lembra.data)
            next_page = request.args.get('next')
            flash('Login efetuado!')
            print('Login efetuado!')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        elif user:
            flash('Senha não confere')
            print('Senha não confere')
        else:
            flash('Usuário não existe')
            print('Usuário não existe')
    return render_template('usuarios/login.html', form=form)


@usuarios.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@usuarios.route('/minha-conta')
@login_required
def account():
    return render_template('usuarios/minha_conta.html')
