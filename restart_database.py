from samba_falado import create_app, db
from samba_falado.models import Letra, Usuario


app = create_app()

app.app_context().push()
db.drop_all()
db.create_all()