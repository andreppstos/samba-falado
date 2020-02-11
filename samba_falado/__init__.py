from flask import Flask

from samba_falado.config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap = Bootstrap(app)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'usuarios.login'
    login_manager.login_message_category = 'info'

    from samba_falado.modules.main.routes import main
    from samba_falado.modules.letras.routes import letras
    from samba_falado.modules.usuarios.routes import usuarios

    app.register_blueprint(main)
    app.register_blueprint(letras)
    app.register_blueprint(usuarios)

    return app


