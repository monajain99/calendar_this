from app import routes  #noqa
from flask import Flask  #noqa
import os

app = Flask (__name__)
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(routes.bp)
