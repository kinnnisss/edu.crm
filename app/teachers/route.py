from flask import render_template, request, redirect, url_for, flash
from app.teachers import teachers_bp
from app.services.teacher_service import TeacherService

service = TeacherService()

@teachers_bp.route('/')
def index():
    teachers = service.listTeachers()
    return render_template('teachers/index.html', teachers=teachers)

@teachers_bp.route('/create', methods=['GET', 'POST'])
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
def delete(teacher_id):
    success = service.deleteTeacher(teacher_id)

    if success:
        flash("Enseignant supprimé.", "success")
    else:
        flash("Erreur : enseignant introuvable.", "danger")

    return redirect(url_for('teachers.index'))