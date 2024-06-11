class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades):
        new_student = Student(name, age, grades)
        self.students.append(new_student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
            print(f"Average Grade: {student.calculate_average_grade():.2f}")
            print("-" * 20)

def main():
    # Create a StudentDatabase instance
    database = StudentDatabase()

    # Add students to the database
    database.add_student("Matt", 20, [85, 90, 78])
    database.add_student("Amanda", 22, [88, 76, 92])
    database.add_student("Ethan", 19, [91, 85, 89])

    # Display all student information
    database.display_all_students()

if __name__ == "__main__":
    main()