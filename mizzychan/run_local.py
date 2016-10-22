#!flask/bin/python
from app import app

app.run(host=app.config['GLOBAL_HOST'], port = app.config['GLOBAL_PORT'], debug = app.config['DEBUG'], threaded=True)
