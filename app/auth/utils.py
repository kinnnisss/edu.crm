from functools import wraps
from flask import session, redirect, url_for, flash
import math


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Veuillez vous connecter pour accéder à cette page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def paginate(items, page=1, per_page=5):
    """
    Pagine une liste d'éléments
    
    Args:
        items (list): Liste des éléments à paginer
        page (int): Numéro de la page (commence à 1)
        per_page (int): Nombre d'éléments par page
    
    Returns:
        tuple: (éléments_paginés, infos_pagination)
    """
    total = len(items)
    total_pages = math.ceil(total / per_page) if total > 0 else 1
    
    # Ajustement de la page
    if page < 1:
        page = 1
    if page > total_pages:
        page = total_pages
    
    # Calcul des indices
    start = (page - 1) * per_page
    end = start + per_page
    
    # Éléments paginés
    paginated_items = items[start:end]
    
    # Informations de pagination
    pagination_info = {
        'page': page,
        'per_page': per_page,
        'total': total,
        'total_pages': total_pages,
        'has_prev': page > 1,
        'has_next': page < total_pages,
        'prev_page': page - 1 if page > 1 else 1,
        'next_page': page + 1 if page < total_pages else total_pages,
        'start_item': start + 1 if total > 0 else 0,
        'end_item': min(end, total)
    }
    
    return paginated_items, pagination_info