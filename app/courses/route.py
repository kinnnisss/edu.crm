# app/courses/route.py
from flask import render_template, request, redirect, url_for, flash

from . import courses_bp
from app.services.course_service import CourseService
from app.services.student_service import StudentService
from app.services.teacher_service import TeacherService

course_service = CourseService()

student_service = StudentService()
teacher_service = TeacherService()


@courses_bp.route("/", methods=["GET"])
def index():
    courses = course_service.listCourses()
    students = student_service.listStudents()
    teachers = teacher_service.listTeachers()
    return render_template(
        "courses/index.html",
        courses=courses,
        students=students,
        teachers=teachers
    )


@courses_bp.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()

    ok = course_service.addCourse(title)
    if ok:
        flash("Cours ajouté avec succès ", "success")
    else:
        flash("Erreur: titre obligatoire ", "danger")

    return redirect(url_for("courses.index"))


@courses_bp.route("/delete/<int:course_id>", methods=["POST"])
def delete(course_id: int):
    ok = course_service.deleteCourse(course_id)
    if ok:
        flash("Cours supprimé ", "success")
    else:
        flash("Suppression impossible: cours introuvable ", "danger")

    return redirect(url_for("courses.index"))


@courses_bp.route("/assign-teacher", methods=["POST"])
def assign_teacher():
    course_id_str = request.form.get("course_id", "").strip()
    teacher_id_str = request.form.get("teacher_id", "").strip()

    try:
        course_id = int(course_id_str)
        teacher_id = int(teacher_id_str)
    except ValueError:
        flash("IDs invalides (doivent être des entiers) ", "danger")
        return redirect(url_for("courses.index"))

    ok = course_service.assignTeacher(course_id, teacher_id, teacher_service)
    if ok:
        flash("Prof assigné au cours ", "success")
    else:
        flash("Erreur: cours ou prof introuvable ", "danger")

    return redirect(url_for("courses.index"))


@courses_bp.route("/assign-students", methods=["POST"])
def assign_students():
    course_id_str = request.form.get("course_id", "").strip()
    student_ids_str_list = request.form.getlist("student_ids")

    try:
        course_id = int(course_id_str)
        student_ids = [int(x) for x in student_ids_str_list]
    except ValueError:
        flash("IDs invalides (doivent être des entiers) ", "danger")
        return redirect(url_for("courses.index"))

    ok = course_service.assignStudents(course_id, student_ids, student_service)
    if ok:
        flash("Étudiants assignés au cours ", "success")
    else:
        flash("Erreur: au moins un étudiant est introuvable ou aucune sélection ", "danger")

    return redirect(url_for("courses.index"))