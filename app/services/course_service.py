# app/services/course_service.py

class CourseService:
    def __init__(self):
        self.courses = [
            {
                "id": 1,
                "title": "Algorithmique",
                "teacher_id": None,
                "student_ids": []
            },
            {
                "id": 2,
                "title": "Programmation Python",
                "teacher_id": None,
                "student_ids": []
            },
            {
                "id": 3,
                "title": "Bases de Données",
                "teacher_id": None,
                "student_ids": []
            },
            {
                "id": 4,
                "title": "Réseaux Informatiques",
                "teacher_id": None,
                "student_ids": []
            },
            {
                "id": 5,
                "title": "Génie Logiciel",
                "teacher_id": None,
                "student_ids": []
            }
        ]
        self.next_id = 6

    def listCourses(self) -> list:
        return self.courses

    def getCourseById(self, course_id: int) -> dict | None:
        for c in self.courses:
            if c["id"] == course_id:
                return c
        return None

    def addCourse(self, title: str) -> bool:
        title = (title or "").strip()
        if not title:
            return False

        course = {
            "id": self.next_id,
            "title": title,
            "teacher_id": None,
            "student_ids": []
        }
        self.courses.append(course)
        self.next_id += 1
        return True

    def deleteCourse(self, course_id: int) -> bool:
        course = self.getCourseById(course_id)
        if course is None:
            return False
        self.courses.remove(course)
        return True

    def assignTeacher(self, course_id: int, teacher_id: int, teacher_service) -> bool:
        course = self.getCourseById(course_id)
        if course is None:
            return False

        teacher = teacher_service.getTeacherById(teacher_id)
        if teacher is None:
            return False

        course["teacher_id"] = teacher_id
        return True

    def assignStudents(self, course_id: int, student_ids: list[int], student_service) -> bool:
        course = self.getCourseById(course_id)
        if course is None:
            return False

        cleaned = []
        for sid in student_ids:
            if sid not in cleaned:
                cleaned.append(sid)

        if len(cleaned) == 0:
            return False

        for sid in cleaned:
            if student_service.getStudentById(sid) is None:
                return False

        course["student_ids"] = cleaned
        return True