class StudentDatabase:
    _student_list = []

    @classmethod
    def add_student(cls, student):
        cls._student_list.append(student)

    @classmethod
    def all_students(cls):
        return cls._student_list

    @classmethod
    def find_student_id(cls, student_id):
        for student in cls._student_list:
            if student.get_student_id() == student_id:
                return student
        return None


class Student:
    def __init__(self, student_id, name, department, is_enrolled=False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def get_student_id(self): 
        return self.__student_id

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id} is already enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} enrolled successfully.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id} is not enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been dropped.")

    def view_student_info(self):
        status = "Enrolled" if self.__is_enrolled else "Not Enrolled"
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Status: {status}")
        print()


Student("001", "Nadia", "Computer Science")
Student("002", "Anika", "English")
Student("003", "Rumi", "Electrical Engineering")


while True:
    print("\n1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    Press = input("Enter your choice (1-4): ")

    if Press == "1":
        print("\n--- All Students ---")
        all_students = StudentDatabase.all_students()
        if not all_students:
            print("No students found.")
        else:
            for student in all_students:
                student.view_student_info()

    elif Press == "2":
        student_id = input("Enter student ID to enroll: ")
        student = StudentDatabase.find_student_id(student_id)
        if student:
            student.enroll_student()
        else:
            print("Student ID not found.")

    elif Press == "3":
        student_id = input("Enter student ID to drop: ")
        student = StudentDatabase.find_student_id(student_id)
        if student:
            student.drop_student()
        else:
            print("Student ID not found.")

    elif Press == "4":
        print("Exit program.")
        break

    else:
        print("Invalid choice.")
