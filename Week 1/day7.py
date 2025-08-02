# Day 7 - Sets

# subset = Teilmenge
# superset = Obermenge

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))

#2
it_companies.add("Twitter")

#3
it_companies.update({"Meta", "Nvidia"})

#4
it_companies.remove("Nvidia")

#5
# discard doesn't raise any errors
it_companies.discard("Nvidiaaaa")

# Level 2

#1
c = A.union(B)

#2
print(A.intersection(B))

#3
print(A.issubset(B))

#4
print(A.isdisjoint(B))

#5
A.update(B)

#6
B.update(A)

#7
del A
del B
del c

# Level 3

#1
age_set = set(age)
print(len(age_set))
print(len(age)) # Set is smaller because only unique members

#2
# String is a array of chars
# list is a collection ordered and changeable
# tuple is a collection of different data types and ordered and unchangeable
# set is collection of items, unordered and un-indexed

#3
str = "I am a teacher and I love to inspire and teach people"
str_list = str.split()
str_set = set(str_list)
print(len(str_list))
print(len(str_set))