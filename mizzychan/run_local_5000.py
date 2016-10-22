#!flask/bin/python
from app import app

app.run(host=app.config['GLOBAL_HOST'], port = 5000, debug = app.config['DEBUG'])
