class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"My Name is {self.name},and my age is {self.age}")

student1 = Student("Saurabh Kharade", 28)
student1.display()