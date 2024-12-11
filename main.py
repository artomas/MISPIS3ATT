class Employee:
    counter = 0

    def __init__(self, s_no, name, email):
        self.s_no = s_no
        self.name = name
        self.email = email
        Employee.counter += 1

    def __str__(self):
        return f"Employee [ID={self.s_no}, Name={self.name}, Email={self.email}]"


class Dean(Employee):
    def make_transfer_of_students(self):
        print(f"Dean {self.name} is transferring students.")

    def expel_student(self, name):
        print(f"Dean {self.name} expelled student {name}.")


class AdministrativeEmployee(Employee):
    def check_equipment(self):
        print(f"Administrative employee {self.name} is checking equipment.")


class ResearchAssociate(Employee):
    def __init__(self, s_no, name, email, field_of_study):
        super().__init__(s_no, name, email)
        self.field_of_study = field_of_study

    def get_field_of_study(self):
        return self.field_of_study

    def set_field_of_study(self, field_of_study):
        self.field_of_study = field_of_study

    def __str__(self):
        return f"Research Associate [Name={self.name}, Field of Study={self.field_of_study}]"


class Lecturer(Employee):
    def __init__(self, s_no, name, email, work_experience):
        super().__init__(s_no, name, email)
        self.work_experience = work_experience

    def take_test(self):
        print(f"Lecturer {self.name} is conducting a test.")

    def tell_the_material(self):
        print(f"Lecturer {self.name} is explaining the material.")


class Course:
    def __init__(self, name, course_id, hours):
        self.name = name
        self.course_id = course_id
        self.hours = hours
        self.teachers = []

    def add_teacher(self, lecturer):
        self.teachers.append(lecturer)

    def __str__(self):
        teachers_names = ", ".join([teacher.name for teacher in self.teachers])
        return f"Course [Name={self.name}, ID={self.course_id}, Hours={self.hours}, Teachers=[{teachers_names}]]"


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        return f"Faculty [Name={self.name}, Departments={self.departments}]"


# Пример использования классов
if __name__ == "__main__":
    dean = Dean(1, "Dr. Smith", "dean@example.com")
    admin_emp = AdministrativeEmployee(2, "John Doe", "admin@example.com")
    researcher = ResearchAssociate(3, "Alice Brown", "alice@example.com", "Physics")
    lecturer = Lecturer(4, "Michael Green", "michael@example.com", 5)

    course = Course("Mathematics", 101, 120)
    course.add_teacher(lecturer)

    faculty = Faculty("Engineering")
    faculty.add_department("Computer Science")

    # Вывод информации
    print(dean)
    dean.make_transfer_of_students()

    print(admin_emp)
    admin_emp.check_equipment()

    print(researcher)
    researcher.set_field_of_study("Quantum Mechanics")
    print(researcher)

    print(lecturer)
    lecturer.tell_the_material()

    print(course)
    print(faculty)
