# Day 13 - List Comprehension
# [i for i in iterable if expression]

#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers_filter = [i for i in numbers if i <= 0]
print(numbers_filter)

#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list1 = [ number for row in list_of_lists for number in row ]
flattened_list2 = [ number for row in flattened_list1 for number in row ]
print(flattened_list2)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

#3
list = []
tuple_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuple_list)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened = [[name.upper(), name[:3].upper(), capital.upper()] for [(name, capital)] in countries]

print(flattened)
