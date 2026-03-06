from flask import render_template, request, redirect, url_for, flash
from . import students_bp
from app.auth.utils import login_required
from app.services.student_service import (
    list_students, create_student, update_student, delete_student, get_student
)


@students_bp.route('/')
@login_required
def index():
    students = list_students()
    return render_template('students/index.html', students=students)


@students_bp.route('/create', methods=['POST'])
@login_required
def create():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    major = request.form.get('major', '').strip()

    if not name or not email or not major:
        flash('Tous les champs sont obligatoires.', 'danger')
        return redirect(url_for('students.index'))

    create_student(name, email, major)
    flash(f'Étudiant "{name}" ajouté avec succès.', 'success')
    return redirect(url_for('students.index'))


@students_bp.route('/update/<int:student_id>', methods=['POST'])
@login_required
def update(student_id):
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    major = request.form.get('major', '').strip()

    if not name or not email or not major:
        flash('Tous les champs sont obligatoires.', 'danger')
        return redirect(url_for('students.index'))

    result = update_student(student_id, name, email, major)
    if result:
        flash(f'Étudiant mis à jour avec succès.', 'success')
    else:
        flash('Étudiant introuvable.', 'danger')

    return redirect(url_for('students.index'))


@students_bp.route('/delete/<int:student_id>', methods=['POST'])
@login_required
def delete(student_id):
    result = delete_student(student_id)
    if result:
        flash('Étudiant supprimé avec succès.', 'success')
    else:
        flash('Étudiant introuvable.', 'danger')
    return redirect(url_for('students.index'))