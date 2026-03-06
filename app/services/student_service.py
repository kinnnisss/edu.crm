# app/services/student_service.py

class StudentService:
    def __init__(self):
        self.students = [
            {"id": 1, "name": "Awa Diop", "email": "awa@example.com", "major": "Informatique"},
            {"id": 2, "name": "Moussa Fall", "email": "moussa@example.com", "major": "Réseaux"},
            {"id": 3, "name": "Fatou Ndiaye", "email": "fatou@example.com", "major": "Génie Logiciel"},
        ]
        self.next_id = 4

    def listStudents(self):
        return self.students

    def getStudentById(self, student_id: int):
        for s in self.students:
            if s["id"] == student_id:
                return s
        return None

    def createStudent(self, name, email, major):
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


# 🔥 Instance globale
_student_service = StudentService()


# 🔥 Fonctions attendues par route.py
def list_students():
    return _student_service.listStudents()

def get_student(student_id):
    return _student_service.getStudentById(student_id)

def create_student(name, email, major):
    return _student_service.createStudent(name, email, major)

def update_student(student_id, name, email, major):
    return _student_service.updateStudent(student_id, name, email, major)

def delete_student(student_id):
    return _student_service.deleteStudent(student_id)