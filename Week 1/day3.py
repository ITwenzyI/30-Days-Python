# Day 3 - Operators

age = int(19)
height = float(1.92)
complex = 1j

def area_triangle():
    base = int(input("Enter Base :" ))
    height = float(input("Enter Height :" ))
    area = 0.5 * height * base
    print("Area :", area)

def perimeter_triangle():
    a = int(input("Enter side a :"))
    b = int(input("Enter side b :"))
    c = int(input("Enter side c :"))
    perimeter = a + b + c
    print("Perimeter :", perimeter)

def rectangle():
    length = int(input("Enter Length :"))
    width = int(input("Enter Width :"))
    area = length * width
    print("Area :", area)
    perimeter = 2 * (length + width)
    print("Perimeter :", perimeter)

pi = 3.14

def circle():
    radius = int(input("Enter Radius :"))
    area = pi * radius * radius
    print("Area :", area)
    circumference = 2 * pi * radius
    print("Circumference :", circumference)

print("Slope :", (10-2) / (6-2))



for x in range(-5,10):
    print("x: ", x, "y :", x ** 2 + 6 * x + 9)

if "on" in ("python" or "dragon"):
    print("Found")

if "jargon" in "I hope this course is not full of jargon":
    print("Found jargon")