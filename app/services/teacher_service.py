class TeacherService:

    # La "base de données" en mémoire
    teachers = [
        {"id": 1, "name": "Dr. Dieng",       "email": "dieng@edu.com",      "speciality": "Algèbre"},
        {"id": 2, "name": "Prof. Coulibaly",  "email": "coulibaly@edu.com",  "speciality": "Intelligence Artificielle"},
        {"id": 3, "name": "Dr. Sylla",        "email": "sylla@edu.com",      "speciality": "Chimie"},
    ]

    next_id = 4

    def listTeachers(self) -> list:
        return self.teachers
    
    def getTeacherById(self, teacher_id: int) -> dict | None:
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                return teacher
        return None

    def addTeacher(self, name: str, email: str, speciality: str) -> bool:
        if not name or not email or not speciality:
            return False
        
        for teacher in self.teachers:
            if teacher["email"] == email:
                return False

        new_teacher = {
            "id":         self.next_id,
            "name":       name,
            "email":      email,
            "speciality": speciality
        }

        self.teachers.append(new_teacher)
        self.next_id += 1
        return True

    def deleteTeacher(self, teacher_id: int) -> bool:
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                self.teachers.remove(teacher)
                return True
        return False