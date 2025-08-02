# Day 6 - Tuples

#1
empty_tuple = ()

#2
siblings_tuple = ("Nikolai", "Antonio")

#3
brothers_tuple = ("Nikolai", "Antonio")
sisters_tuple = ("Zoldyck", "Gotti")
siblings = brothers_tuple + siblings_tuple

#4
print(len(siblings))

#5
family = ("Imagine", "No Way") + siblings

# Level 2

#2
fruits = ("Apple", "Orange")
vegetables = ("Tomato", "Salad")
animal_products = ("Milk", "Cheese")
food_stuff_tp = fruits + vegetables + animal_products

#3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#4
middle_index = len(food_stuff_tp)//2
print(food_stuff_tp[middle_index])
print(food_stuff_lt[middle_index])

#5
print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)