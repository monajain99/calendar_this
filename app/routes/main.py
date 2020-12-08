from flask import Blueprint

bp = Blueprint('', __name__)

@bp.route('/')
def index():
  return '<h1>Hello</h1>'











# from flask import Blueprint, render_template, redirect
# from app.forms.login import LoginForm

# bp = Blueprint('', __name__)







