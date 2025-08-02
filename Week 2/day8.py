# Day 8 - Dictionary
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#1
dog = {}

#2
dog["name"] = "Zoe"
dog["color"] = "blue"
dog["breed"] = "Jack Russel"
dog["legs"] = 4
dog["age"] = 8
print(dog)

#3
student = {
    "first_name": "Zoe",
    "last_name": "Russel",
    "gender": "male",
    "age": 8,
    "marital_status": "married",
    "skills" : ["Python", "C++"],
    "country": "US",
    "city": "New York",
    "address": "Street Address"
}

#4
print(len(student))

#5
print(student["skills"])
print(type(student["skills"]))

#6
student["skills"].append("C")
student["skills"].append("Lua")
print(student["skills"])

#7
print(student.keys())

#8
print(student.values())

#9
print(student.items())

#10
del student["gender"]

#11
del dog
