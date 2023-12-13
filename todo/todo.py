from flask import Blueprint, render_template



bp = Blueprint('todo', __name__, url_prefix='/todo')
from todo.auth import login_required

@bp.route('/list')
@login_required
def index():
    return render_template('todor/index.html')

@bp.route('/create')
def create():
    return render_template('') 

