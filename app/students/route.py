from flask import render_template, request, redirect, url_for, flash
from . import students_bp
from app.services.student_service import StudentService
from app.auth.utils import login_required
from app.auth.utils import paginate

service = StudentService()

@students_bp.route('/')
@login_required
def home():
    return redirect(url_for('students.list_students'))

@students_bp.route('/students')
@login_required
def list_students():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 3, type=int)
    search = request.args.get('search', '').strip()
    major = request.args.get('major', '').strip()

    students = service.searchStudents(search=search, major=major)
    students_paginated, pagination_info = paginate(students, page, per_page)

    return render_template(
        'students/index.html',
        students=students_paginated,
        pagination=pagination_info,
        search=search,
        selected_major=major,
        majors=service.getMajors()
    )

@students_bp.route('/students/<int:id>')
@login_required
def show_student(id):
    student = service.getStudentById(id)

    if not student:
        flash("Étudiant introuvable.", "danger")
        return redirect(url_for('students.list_students'))

    return render_template('students/show.html', student=student)

@students_bp.route('/students/add', methods=['POST'])
@login_required
def add_student():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    major = request.form.get('major', '').strip()

    action = service.addStudent(name, email, major)

    if action:
        flash("Étudiant ajouté avec succès !", "success")
    else:
        flash("Erreur : champs manquants ou email déjà utilisé.", "danger")

    return redirect(url_for('students.list_students'))

@students_bp.route('/students/edit/<int:id>', methods=['POST'])
@login_required
def edit_student(id):
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    major = request.form.get('major', '').strip()

    action = service.updateStudent(id, name, email, major)

    if action:
        flash("Étudiant modifié avec succès !", "success")
    else:
        flash("Erreur : données invalides ou email déjà utilisé.", "danger")

    return redirect(url_for('students.list_students'))

@students_bp.route('/students/delete/<int:id>')
@login_required
def delete_student(id):
    action = service.deleteStudent(id)

    if action:
        flash("Étudiant supprimé avec succès.", "success")
    else:
        flash("Étudiant introuvable.", "danger")

    return redirect(url_for('students.list_students'))