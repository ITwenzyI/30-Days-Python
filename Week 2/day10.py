# Day 10 - Loops
# while and for Loop

#1
# for i in range(0, 11):
#     print(i)
#
# i = 0
# while i <= 10:
#     print(i)
#     i = i + 1

#2
x = 10
for i in range(0, 11):
    print(x)
    x = x - 1
x = 10
while x >= 0:
    print(x)
    x = x - 1

#3
hashh = "#######"
print(hashh[0])
for i in range(1, 8):
    print(hashh[:i])

#4
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()

#5
for num in range(0, 11):
    print(f"{num} * {num} = {num * num}")

#6
name_lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for name in name_lst:
    print(name)

#7
for i in range(0, 101, 2):
    print(i)

#8
for i in range(0, 101):
    if i % 2 == 1:
        print(i)
    if not i % 2 == 0:
        print(i)


# Level 2

#1
x = 0
for i in range(0, 101):
    x += i
print(f"The sum of all numbers ist {x}")

#2
even = 0
odd = 0
for i in range(0, 101):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f"The sum of all even numbers is: {even}, The sum of all odd numbers is: {odd}")

#3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  "Testland",
  'Bolivia'
]
for country in countries:
    if "land" in country:
        print(country)

#2
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
for fruit in fruits:
    print(fruit)