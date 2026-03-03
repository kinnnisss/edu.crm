class StudentService:
    def __init__(self):
        self.students = [
            {"id": 1, "name": "Awa Diop", "email": "awa@example.com"},
            {"id": 2, "name": "Moussa Fall", "email": "moussa@example.com"},
            {"id": 3, "name": "Fatou Ndiaye", "email": "fatou@example.com"},
        ]

    def listStudents(self):
        return self.students

    def getStudentById(self, student_id: int):
        for s in self.students:
            if s["id"] == student_id:
                return s
        return None