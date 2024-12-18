class Employee:
    counter = 0

    def __init__(self, s_no, name, email):
        self.s_no = s_no
        self.name = name
        self.email = email
        Employee.counter += 1

    def __str__(self):
        return f"Сотрудник [ID={self.s_no}, Имя={self.name}, Email={self.email}]"


class Dean(Employee):
    def __init__(self, s_no, name, email):
        super().__init__(s_no, name, email)
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.s_no != student_id]

    def make_transfer_of_students(self):
        return f"Декан {self.name} переводит студентов."

    def expel_student(self, name):
        return f"Декан {self.name} исключил студента {name}."

    def list_students(self):
        if not self.students:
            return f"У декана {self.name} нет студентов."
        student_list = "\n".join(str(student) for student in self.students)
        return f"Студенты декана {self.name}:\n{student_list}"


class AdministrativeEmployee(Employee):
    def check_equipment(self):
        return f"Административный сотрудник {self.name} проверяет оборудование."


class ResearchAssociate(Employee):
    def __init__(self, s_no, name, email, field_of_study):
        super().__init__(s_no, name, email)
        self.field_of_study = field_of_study

    def get_field_of_study(self):
        return self.field_of_study

    def set_field_of_study(self, field_of_study):
        self.field_of_study = field_of_study

    def __str__(self):
        return f"Научный сотрудник [Имя={self.name}, Область исследований={self.field_of_study}]"


class Lecturer(Employee):
    def __init__(self, s_no, name, email, work_experience):
        super().__init__(s_no, name, email)
        self.work_experience = work_experience

    def take_test(self):
        return f"Преподаватель {self.name} проводит тест."

    def tell_the_material(self):
        return f"Преподаватель {self.name} объясняет материал."


class Course:
    def __init__(self, name, course_id, hours):
        self.name = name
        self.course_id = course_id
        self.hours = hours
        self.teachers = []
        self.students = []

    def add_teacher(self, lecturer):
        self.teachers.append(lecturer)

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        teachers_names = ", ".join([teacher.name for teacher in self.teachers])
        students_names = ", ".join([student.name for student in self.students])
        return (f"Курс [Название={self.name}, ID={self.course_id}, Часы={self.hours}, "
                f"Преподаватели=[{teachers_names}], Студенты=[{students_names}]]")


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        departments_str = ", ".join(self.departments)
        return f"Факультет [Название={self.name}, Отделения=[{departments_str}]]"


class Student:
    def __init__(self, s_no, name, email):
        self.s_no = s_no
        self.name = name
        self.email = email

    def __str__(self):
        return f"Студент [ID={self.s_no}, Имя={self.name}, Email={self.email}]"


if __name__ == "__main__":
    # Пример работы
    dean = Dean(1, "Евгений Кулешов", "dean@example.com")
    admin_emp = AdministrativeEmployee(2, "Максим Попов", "admin@example.com")
    researcher = ResearchAssociate(3, "Никита фролов", "alice@example.com", "Физика")
    lecturer = Lecturer(4, "Михаил Дубов", "michael@example.com", 5)

    student1 = Student(101, "Иван Иванов", "ivan@example.com")
    student2 = Student(102, "Анна Смирнова", "anna@example.com")

    dean.add_student(student1)
    dean.add_student(student2)

    course = Course("Математика", 101, 120)
    course.add_teacher(lecturer)
    course.add_student(student1)
    course.add_student(student2)

    faculty = Faculty("Инженерный")
    faculty.add_department("Компьютерные науки")

    print(dean)
    print(dean.make_transfer_of_students())
    print(dean.list_students())

    print(admin_emp)
    print(admin_emp.check_equipment())

    print(researcher)
    researcher.set_field_of_study("Квантовая механика")
    print(researcher)

    print(lecturer)
    print(lecturer.tell_the_material())

    print(course)
    print(faculty)
