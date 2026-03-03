# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-secret-key"

    # Blueprints
    from app.courses import courses_bp
    from app.auth import auth_bp
    app.register_blueprint(courses_bp, url_prefix="/courses")
    app.register_blueprint(auth_bp)
    # from app.students import students_bp
    # app.register_blueprint(students_bp, url_prefix="/students")
    # from app.teachers import teachers_bp
    # app.register_blueprint(teachers_bp, url_prefix="/teachers")

#seulement pour tester mon blueprint courses
    @app.route("/")
    def home():
        return "Edu.CRM OK ! (Va sur /courses)"

    return app