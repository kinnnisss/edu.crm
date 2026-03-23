from flask import render_template, request, redirect, url_for, flash
from . import teachers_bp
from app.services.teacher_service import TeacherService
from app.auth.utils import login_required
from app.auth.utils import paginate

service = TeacherService()

@teachers_bp.route('')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)
    search = request.args.get('search', '').strip()
    speciality = request.args.get('speciality', '').strip()

    teachers = service.searchTeachers(search=search, speciality=speciality)
    teachers_paginated, pagination_info = paginate(teachers, page, per_page)

    return render_template(
        'teachers/index.html',
        teachers=teachers_paginated,
        pagination=pagination_info,
        search=search,
        selected_speciality=speciality,
        specialities=service.getSpecialities()
    )

@teachers_bp.route('/<int:teacher_id>')
@login_required
def show(teacher_id):
    teacher = service.getTeacherById(teacher_id)

    if not teacher:
        flash("Enseignant introuvable.", "danger")
        return redirect(url_for('teachers.index'))

    return render_template('teachers/show.html', teacher=teacher)

@teachers_bp.route('/create', methods=['POST'])
@login_required
def create():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    speciality = request.form.get('speciality', '').strip()

    success = service.addTeacher(name, email, speciality)

    if success:
        flash("Enseignant ajouté avec succès !", "success")
    else:
        flash("Erreur : champs manquants ou email déjà utilisé.", "danger")

    return redirect(url_for('teachers.index'))

@teachers_bp.route('/edit/<int:teacher_id>', methods=['POST'])
@login_required
def edit(teacher_id):
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    speciality = request.form.get('speciality', '').strip()

    success = service.updateTeacher(teacher_id, name, email, speciality)

    if success:
        flash("Enseignant modifié avec succès !", "success")
    else:
        flash("Erreur : données invalides ou email déjà utilisé.", "danger")

    return redirect(url_for('teachers.index'))

@teachers_bp.route('/delete/<int:teacher_id>', methods=['POST'])
@login_required
def delete(teacher_id):
    success = service.deleteTeacher(teacher_id)

    if success:
        flash("Enseignant supprimé.", "success")
    else:
        flash("Erreur : enseignant introuvable.", "danger")

    return redirect(url_for('teachers.index'))