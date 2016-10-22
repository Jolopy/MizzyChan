from flask import Flask
from flask_mail import Mail
import os

app = Flask(__name__)

app.config.from_pyfile('../config.py')

initPath = os.path.dirname(os.path.realpath(__file__))

app.config.update()

mail=Mail(app)

#getattr(client, authenticationDatabase)

from app import views



