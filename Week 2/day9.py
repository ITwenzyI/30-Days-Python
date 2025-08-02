# Day 9 - Conditionals
# if, elif, else ...

#1
age = int(input("Enter Age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    age_difference = 18 - age
    print(f"You need {age_difference} years to learn to drive.")


#3
number_one = int(input("Enter number one: "))
number_two = int(input("Enter number two: "))
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one == number_two:
    print(f"{number_one} is equal to {number_two}")
else:
    print(f"{number_one} is less than {number_two}")

# Level 2

#1
score = 0
if 80 <= score <= 100:
    print("A")
elif 70 <= score <= 89:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
else:
    print("F")

#2
month = input("Enter Month: ")
month = month.lower()
if "september" or "october" or "november" == month:
    print("Autumn")
else:
    print("Winter")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter fruit: ")
if not fruit in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exist in the list')

# Level 3

#1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if person["skills"]:
    middle_index = len(person["skills"]) // 2
    print(person["skills"][middle_index])

if person["skills"] and "Python" in person["skills"] :
    print("Python")

if person["skills"] and person["skills"] == ["JavaScript", "React"]:
    print("He is a front end developer")
elif person["skills"] == ["Node", "MongoDB", "Python"]:
    print("He is a backend developer")
elif person["skills"] == ["MongoDB", "React", "Node"]:
    print("He is a fullstack developer")
else:
    print("Unknown title")

if person["is_marred"] and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")