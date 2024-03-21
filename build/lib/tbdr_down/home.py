from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
bp = Blueprint('home', __name__)


@bp.route('/',methods=('GET', 'POST'))
def index():
    return render_template('pages/index.html')

