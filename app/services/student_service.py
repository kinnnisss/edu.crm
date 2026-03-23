class StudentService:
    def __init__(self):
        self.students = [
            {"id": 1, "name": "Awa Diop", "email": "awa@example.com", "major": "Informatique"},
            {"id": 2, "name": "Moussa Fall", "email": "moussa@example.com", "major": "Réseaux"},
            {"id": 3, "name": "Fatou Ndiaye", "email": "fatou@example.com", "major": "Génie Logiciel"},
        ]
        self.next_id = 4

    def listStudents(self) -> list:
        return sorted(self.students, key=lambda s: s["id"], reverse=True)

    def getStudentById(self, student_id):
        for s in self.students:
            if s["id"] == student_id:
                return s
        return None

    def getMajors(self) -> list:
        majors = []
        for student in self.students:
            major = student.get("major")
            if major and major not in majors:
                majors.append(major)
        return sorted(majors)

    def searchStudents(self, search="", major="") -> list:
        results = self.listStudents()

        if search:
            search_lower = search.lower()
            results = [
                s for s in results
                if search_lower in s.get("name", "").lower()
                or search_lower in s.get("email", "").lower()
            ]

        if major:
            results = [
                s for s in results
                if s.get("major", "") == major
            ]

        return results

    def isEmailUnique(self, email, exclude_id=None) -> bool:
        for student in self.students:
            if student["email"].lower() == email.lower():
                if exclude_id is None or student["id"] != exclude_id:
                    return False
        return True

    def addStudent(self, name, email, major):
        name = name.strip() if name else ""
        email = email.strip() if email else ""
        major = major.strip() if major else ""

        if not name or not email or not major:
            return False

        if not self.isEmailUnique(email):
            return False

        student = {
            "id": self.next_id,
            "name": name,
            "email": email,
            "major": major
        }
        self.students.append(student)
        self.next_id += 1
        return True

    def updateStudent(self, student_id, name, email, major):
        student = self.getStudentById(student_id)
        if not student:
            return False

        name = name.strip() if name else ""
        email = email.strip() if email else ""
        major = major.strip() if major else ""

        if not name or not email or not major:
            return False

        if not self.isEmailUnique(email, exclude_id=student_id):
            return False

        student["name"] = name
        student["email"] = email
        student["major"] = major
        return True

    def deleteStudent(self, student_id):
        student = self.getStudentById(student_id)
        if not student:
            return False
        self.students.remove(student)
        return True