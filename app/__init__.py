from flask import Flask

def create_app():
    app = Flask(__name__) 
    app.config["SECRET_KEY"] = "dev-secret-key"

    # Blueprints
    from app.auth import auth_bp
    from app.students import students_bp
    from app.teachers import teachers_bp
    from app.courses import courses_bp
    from app.dashboard import dashboard_bp  

    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp, url_prefix="/students")
    app.register_blueprint(teachers_bp, url_prefix="/teachers")
    app.register_blueprint(courses_bp, url_prefix="/courses")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

    return app