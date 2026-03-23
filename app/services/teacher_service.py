class TeacherService:
    teachers = [
        {"id": 1, "name": "Dr. Dieng", "email": "dieng@edu.com", "speciality": "Algèbre"},
        {"id": 2, "name": "Prof. Coulibaly", "email": "coulibaly@edu.com", "speciality": "Intelligence Artificielle"},
        {"id": 3, "name": "Dr. Sylla", "email": "sylla@edu.com", "speciality": "Chimie"},
    ]

    next_id = 4

    def listTeachers(self) -> list:
        return sorted(self.teachers, key=lambda teacher: teacher["id"], reverse=True)

    def getTeacherById(self, teacher_id: int) -> dict | None:
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                return teacher
        return None

    def getSpecialities(self) -> list:
        specialities = []
        for teacher in self.teachers:
            speciality = teacher.get("speciality")
            if speciality and speciality not in specialities:
                specialities.append(speciality)
        return sorted(specialities)

    def searchTeachers(self, search: str = "", speciality: str = "") -> list:
        teachers = self.listTeachers()

        if search:
            search_lower = search.lower()
            teachers = [
                teacher for teacher in teachers
                if search_lower in teacher.get("name", "").lower()
                or search_lower in teacher.get("email", "").lower()
            ]

        if speciality:
            teachers = [
                teacher for teacher in teachers
                if teacher.get("speciality", "") == speciality
            ]

        return teachers

    def isEmailUnique(self, email: str, exclude_id: int | None = None) -> bool:
        for teacher in self.teachers:
            if teacher["email"].lower() == email.lower():
                if exclude_id is None or teacher["id"] != exclude_id:
                    return False
        return True

    def addTeacher(self, name: str, email: str, speciality: str) -> bool:
        name = name.strip() if name else ""
        email = email.strip() if email else ""
        speciality = speciality.strip() if speciality else ""

        if not name or not email or not speciality:
            return False

        if not self.isEmailUnique(email):
            return False

        new_teacher = {
            "id": self.next_id,
            "name": name,
            "email": email,
            "speciality": speciality
        }

        self.teachers.append(new_teacher)
        self.next_id += 1
        return True

    def updateTeacher(self, teacher_id: int, name: str, email: str, speciality: str) -> bool:
        teacher = self.getTeacherById(teacher_id)

        if not teacher:
            return False

        name = name.strip() if name else ""
        email = email.strip() if email else ""
        speciality = speciality.strip() if speciality else ""

        if not name or not email or not speciality:
            return False

        if not self.isEmailUnique(email, exclude_id=teacher_id):
            return False

        teacher["name"] = name
        teacher["email"] = email
        teacher["speciality"] = speciality
        return True

    def deleteTeacher(self, teacher_id: int) -> bool:
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                self.teachers.remove(teacher)
                return True
        return False