import unittest

from main import Employee, Dean, Student, Course, Lecturer,ResearchAssociate


class TestUniversitySystem(unittest.TestCase):

    def test_employee_creation(self):
        emp = Employee(1, "Иван Иванов", "ivan@example.com")
        self.assertEqual(emp.s_no, 1)
        self.assertEqual(emp.name, "Иван Иванов")
        self.assertEqual(emp.email, "ivan@example.com")

    def test_dean_add_student(self):
        dean = Dean(1, "Евгений Кулешов", "dean@example.com")
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        dean.add_student(student1)
        self.assertEqual(len(dean.students), 1)
        self.assertEqual(dean.students[0].name, "Иван Иванов")

    def test_dean_remove_student(self):
        dean = Dean(1, "Евгений Кулешов", "dean@example.com")
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        student2 = Student(102, "Анна Смирнова", "anna@example.com")
        dean.add_student(student1)
        dean.add_student(student2)
        dean.remove_student(101)
        self.assertEqual(len(dean.students), 1)
        self.assertEqual(dean.students[0].name, "Анна Смирнова")

    def test_dean_list_students(self):
        dean = Dean(1, "Евгений Кулешов", "dean@example.com")
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        student2 = Student(102, "Анна Смирнова", "anna@example.com")
        dean.add_student(student1)
        dean.add_student(student2)
        student_list = dean.list_students()
        self.assertIn("Иван Иванов", student_list)
        self.assertIn("Анна Смирнова", student_list)

    def test_course_add_student(self):
        course = Course("Математика", 101, 120)
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        course.add_student(student1)
        self.assertEqual(len(course.students), 1)
        self.assertEqual(course.students[0].name, "Иван Иванов")

    def test_course_add_teacher(self):
        course = Course("Математика", 101, 120)
        lecturer = Lecturer(4, "Михаил Дубов", "michael@example.com", 5)
        course.add_teacher(lecturer)
        self.assertEqual(len(course.teachers), 1)
        self.assertEqual(course.teachers[0].name, "Михаил Дубов")

    def test_researcher_field_of_study(self):
        researcher = ResearchAssociate(3, "Никита Фролов", "alice@example.com", "Физика")
        self.assertEqual(researcher.get_field_of_study(), "Физика")
        researcher.set_field_of_study("Квантовая механика")
        self.assertEqual(researcher.get_field_of_study(), "Квантовая механика")

    def test_lecturer_work_experience(self):
        lecturer = Lecturer(4, "Михаил Дубов", "michael@example.com", 5)
        self.assertEqual(lecturer.work_experience, 5)

if __name__ == "__main__":
    unittest.main()
