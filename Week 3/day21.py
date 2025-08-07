# Day 21 - Classes

class Person:
    def __init__(self, name= "Kilian", age = 19):
        self.name = name
        self.age = age
        self.skills = []

    def print_person(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def add_skill(self, skill):
        self.skills.append(skill)

class FakePerson(Person):
    def __init__(self, name= "Kilian", age = 19, gender="Male"):
        super().__init__(name, age)
        self.gender = gender

p = Person()
p.print_person()
p1 = Person("Nikolai", 21)
p1.print_person()
p1.add_skill("Python")
print(p1.skills)

fp = FakePerson()
fp.print_person()