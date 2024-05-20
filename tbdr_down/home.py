from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
bp = Blueprint('home', __name__)


@bp.route('/<path:path>',methods=('GET', 'POST'))
def index(path):
    return render_template('pages/index.html')

