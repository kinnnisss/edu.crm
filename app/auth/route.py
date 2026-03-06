from flask import render_template, request, redirect, url_for, flash, session
from . import auth_bp
from .utils import login_required

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['user'] = username
            flash('Connexion réussie. Bienvenue !', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Identifiants incorrects. Veuillez réessayer.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.login'))