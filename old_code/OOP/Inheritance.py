class Person:
    def __init__(self):
        self.first_name = None
        self.last_name = None

    def _create(self, first_name, last_name):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        return self

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher:
    def __init__(self):
        self.first_name = None
        self.last_name = None

    def _create(self, first_name, last_name):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        return self

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = None

    def create_student(self, first_name, last_name, student_id):
        super()._create(first_name, last_name)
        self.student_id = student_id
        return self

    def __str__(self):
        return f"{super().__str__()} {self.student_id}"


class StudentTeacher(Person, Teacher):
    pass


if __name__ == '__main__':
    student = Student().create_student(
        first_name="Max",
        last_name="Curtis",
        student_id=1
    )
    print(student)
