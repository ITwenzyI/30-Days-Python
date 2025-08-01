# Day 4 - Strings

space = " "

#1
complete_str = "Thirty" + space + "Days" + space + "Of" + space + "Python"
print(complete_str)

#2
complete_str = "Coding" + space + "for" + space + "All"
print(complete_str)

#3
company = "Coding For All"

#4
print(company)

#5
print(len(company))

#6
print(company.upper())

#7
print(company.lower())

#8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9
print(company[0:7])

#10
print(company.find("Coding"))
print(company.index("Coding"))
print(company.rfind("Coding"))

#11
print(company.replace("Coding", "Python"))

#13
print(company.split())

#14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

#15
print(company[0])

#16
print(company[-1])

#17
print(company[10])

#20
print(company.rfind("I"))

#21
print(company.index("F"))

#22
print(company.index("A"))

# 23-24
strr = "You cannot end a sentence with because because because is a conjunction"
print(strr.index("because"))
print(strr.rindex("because"))

#25
str_slice = strr[31:54]
print(str_slice)

#28
print(company.startswith("Coding"))

#29
print(company.endswith("Coding"))

#30
print("  Coding For All      ".strip())
print("  Coding For All      ".lstrip())
print("  Coding For All      ".rstrip())

#32
names = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " # ".join(names)
print(result)

#34
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of the circle with radius {radius} is {area} meters square")

#36
print(f"{8} + {6} = {14}")
print("8 + 6 = 14")

