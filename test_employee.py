import unittest

from main import Employee, Dean, AdministrativeEmployee, ResearchAssociate, Lecturer, Course, Faculty, Student

class TestUniversitySystem(unittest.TestCase):

    def setUp(self):
        Employee.counter = 0

    def test_employee_creation(self):
        emp = Employee(1, "Иван Иванов", "ivan@example.com")
        self.assertEqual(emp.s_no, 1)
        self.assertEqual(emp.name, "Иван Иванов")
        self.assertEqual(emp.email, "ivan@example.com")
        self.assertEqual(Employee.counter, 1)

    def test_dean_add_and_remove_student(self):
        dean = Dean(1, "Евгений Кулешов", "dean@example.com")
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        student2 = Student(102, "Анна Смирнова", "anna@example.com")

        dean.add_student(student1)
        dean.add_student(student2)

        self.assertEqual(len(dean.students), 2)
        self.assertIn(student1, dean.students)
        self.assertIn(student2, dean.students)

        dean.remove_student(101)
        self.assertEqual(len(dean.students), 1)
        self.assertNotIn(student1, dean.students)
        self.assertIn(student2, dean.students)

    def test_dean_list_students(self):
        dean = Dean(1, "Евгений Кулешов", "dean@example.com")
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        student2 = Student(102, "Анна Смирнова", "anna@example.com")

        dean.add_student(student1)
        dean.add_student(student2)
        student_list = dean.list_students()

        self.assertIn("Иван Иванов", student_list)
        self.assertIn("Анна Смирнова", student_list)

    def test_course_add_student_and_teacher(self):
        course = Course("Математика", 101, 120)
        student1 = Student(101, "Иван Иванов", "ivan@example.com")
        lecturer = Lecturer(4, "Михаил Дубов", "michael@example.com", 5)

        course.add_student(student1)
        course.add_teacher(lecturer)

        self.assertEqual(len(course.students), 1)
        self.assertEqual(len(course.teachers), 1)
        self.assertIn(student1, course.students)
        self.assertIn(lecturer, course.teachers)

    def test_research_associate_field_of_study(self):
        researcher = ResearchAssociate(3, "Никита Фролов", "alice@example.com", "Физика")
        self.assertEqual(researcher.get_field_of_study(), "Физика")

        researcher.set_field_of_study("Квантовая механика")
        self.assertEqual(researcher.get_field_of_study(), "Квантовая механика")

    def test_administrative_employee_check_equipment(self):
        admin_emp = AdministrativeEmployee(2, "Максим Попов", "admin@example.com")
        self.assertEqual(admin_emp.check_equipment(), "Административный сотрудник Максим Попов проверяет оборудование.")

    def test_lecturer_methods(self):
        lecturer = Lecturer(4, "Михаил Дубов", "michael@example.com", 5)
        self.assertEqual(lecturer.tell_the_material(), "Преподаватель Михаил Дубов объясняет материал.")
        self.assertEqual(lecturer.take_test(), "Преподаватель Михаил Дубов проводит тест.")

    def test_faculty_add_department(self):
        faculty = Faculty("Инженерный")
        faculty.add_department("Компьютерные науки")
        self.assertIn("Компьютерные науки", faculty.departments)
        self.assertEqual(str(faculty), "Факультет [Название=Инженерный, Отделения=[Компьютерные науки]]")


if __name__ == "__main__":
    unittest.main()
