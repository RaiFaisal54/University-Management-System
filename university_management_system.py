class UniversityMember:
    def __init__(self, name, member_id):
        self.name = name
        self._member_id = member_id

    def show_role(self):
        print("University Member")

    def show_details(self):
        print("Name:", self.name)
        print("ID:", self._member_id)


class Student(UniversityMember):
    def __init__(self, name, member_id, course):
        super().__init__(name, member_id)
        self.course = course
        self.__gpa = 0.0
        self.__fee = 0

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if gpa < 0 or gpa > 4:
            print("Invalid GPA! GPA must be between 0 and 4.")
        else:
            self.__gpa = gpa

    def get_fee(self):
        return self.__fee

    def set_fee(self, fee):
        self.__fee = fee

    def show_role(self):
        print("Role: Student")

    def show_details(self):
        print("Name:", self.name)
        print("ID:", self._member_id)
        print("Course:", self.course)
        print("GPA:", self.__gpa)
        print("Fee:", self.__fee)


class GraduateStudent(Student):
    def __init__(self, name, member_id, course, research_topic):
        super().__init__(name, member_id, course)
        self.research_topic = research_topic

    def show_role(self):
        print("Role: Graduate Student")

    def show_details(self):
        super().show_details()
        print("Research Topic:", self.research_topic)


# Main program
students = []

while True:
    print("\n---- University Management System ----")
    print("1. Add Student Record")
    print("2. Display All Student Records")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        sid = input("Enter Student ID: ")
        course = input("Enter Course Name: ")

        try:
            gpa = float(input("Enter GPA: "))
            fee = int(input("Enter Fee Amount: "))
        except ValueError:
            print("Invalid GPA or fee. Please enter a number.")
            continue

        grad = input("Is this a graduate student? (yes/no): ")

        if grad.lower() == "yes":
            topic = input("Enter Research Topic: ")
            student = GraduateStudent(name, sid, course, topic)
        else:
            student = Student(name, sid, course)

        student.set_gpa(gpa)
        student.set_fee(fee)
        students.append(student)
        print("Student record added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\n--- ALL Student Records ---")
            for student in students:
                student.show_role()
                student.show_details()

    elif choice == "3":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
