class Student:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    def get_info(self):
        print(f"students: {self.name} {self.last_name}")
class School:
    def __init__(self, school_name, address):
        self.school_name = school_name
        self.address = address
        self.students = []
    def add_student(self, student_obj):
        self.students.append(student_obj)
        print(f"system: {student_obj.name} kid was accepted idk")
    def remove_student(self, index):
        if 0 <= index < len(self.students):
            removed = self.students.pop(index)
            print(f"system: student {removed.name} student is deleted")
        else:
            print("student doesnt exist")
    def show_students(self):
        print(f"\n- {self.school_name}-students list-")
        if not self.students:
            print("list is empty")
        for student in self.students:
            student.get_info()
        print("------------------------------------------\n")
my_school = School("Tbilisis N67 public school", "gvazauris metro N67")
s1 = Student("Anano", "Papidze", 14)
s2 = Student("Mimi", "metreveli", 16)
s3 = Student("elene", "gamsaxudria", 15)
s4 = Student("gigi", "chachanidze", 17)
my_school.add_student(s1)
my_school.add_student(s2)
my_school.add_student(s3)
my_school.add_student(s4)
my_school.show_students()
my_school.remove_student(1)
my_school.show_students()