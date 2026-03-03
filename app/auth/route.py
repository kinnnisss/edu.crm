from flask import render_template, request, redirect, url_for, session, flash
from functools import wraps
from . import auth_bp  

ADMIN = {
    'username': 'admin',
    'password': 'admin123'
}

def login_required(f):
    """Décorateur pour protéger les routes"""
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Veuillez vous connecter', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Page de connexion"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN['username'] and password == ADMIN['password']:
            session['user_id'] = 1
            session['username'] = username
            flash('Connexion réussie', 'success')
            # à changé plutard par auth.dashboard
            return redirect(url_for('auth.dashboard_provisoire'))
        else:
            flash('Identifiants incorrects', 'error')
    
    return render_template('auth/login.html')   

@auth_bp.route('/logout')
def logout():
    """Déconnexion"""
    session.clear()
    flash('Déconnexion réussie', 'success')
    return redirect(url_for('auth.login'))

# j'ai creer cette route pour tester (à supprimer quand dashboard sera créé)
@auth_bp.route('/dashboard-provisoire')
def dashboard_provisoire():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return f"<h1>Connexion réussie !</h1><p>Connecté en tant que {session['username']}</p><p><a href='{url_for('auth.logout')}'>Déconnexion</a></p>"