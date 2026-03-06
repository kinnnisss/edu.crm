from flask import render_template
from . import dashboard_bp
from app.auth.utils import login_required
from app.services import student_service, teacher_service, course_service


@dashboard_bp.route('/')
@login_required
def index():
    return render_template('dashboard/index.html',
        total_students=len(student_service.listStudents()),
        total_teachers=len(teacher_service.listTeachers()),
        total_courses=len(course_service.listCourses()),
        courses=course_service.listCourses()
    )