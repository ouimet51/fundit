from app import app, db
from app.models import User,Fund,Contribution,Transfer


@app.shell_context_processor
def make_shell_context():
    return {'db': db,'User': User,'Fund':Fund,'Contribution':Contribution,'Transfer':Transfer}
