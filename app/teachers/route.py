from flask import render_template, request, redirect, url_for, flash
from . import teachers_bp
from app.services.teacher_service import TeacherService
from app.auth.utils import login_required
from app.auth.utils import paginate


service = TeacherService()

@teachers_bp.route('')
@login_required
def index():
    """Liste des enseignants avec pagination"""
    
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)
    
    teachers = service.listTeachers()
    teachers_paginated, pagination_info = paginate(teachers, page, per_page)
    
    return render_template(
        'teachers/index.html',
        teachers=teachers_paginated,
        pagination=pagination_info
    )
@teachers_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        name       = request.form.get('name')
        email      = request.form.get('email')
        speciality = request.form.get('speciality')

        success = service.addTeacher(name, email, speciality)

        if success:
            flash("Enseignant ajouté avec succès !", "success")
        else:
            flash("Erreur : champs manquants ou email déjà utilisé.", "danger")

        return redirect(url_for('teachers.index'))

    return render_template('teachers/index.html', teachers=service.listTeachers())

@teachers_bp.route('/delete/<int:teacher_id>', methods=['POST'])
@login_required
def delete(teacher_id):
    success = service.deleteTeacher(teacher_id)

    if success:
        flash("Enseignant supprimé.", "success")
    else:
        flash("Erreur : enseignant introuvable.", "danger")

    return redirect(url_for('teachers.index'))