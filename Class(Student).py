class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_info(self):
        return self.name + " has grade " + str(self.grade)

    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False

# Create two students
student1 = Student("Ali", 85)
student2 = Student("Sara", 55)

# Test the methods
print(student1.get_info())
print("Passing?", student1.is_passing())

print(student2.get_info())
print("Passing?", student2.is_passing())