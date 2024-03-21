from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
bp = Blueprint('home', __name__)


@bp.route('/',methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        flash(request.form)
        if "script_name" in request.form:
                return redirect(url_for('home.args', scriptname=request.form['script_name']))

    return render_template('pages/index.html')

