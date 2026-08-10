class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} scored {self.grade}%")

    def is_passing(self):
        return self.grade >= 60


emma = Student("Emma", 85)
liam = Student("Liam", 45)

emma.display()
print("Passing:", emma.is_passing())

liam.display()
print("Passing:", liam.is_passing())