# Day 11 - Functions
# def ...
import math


#1
def add_two_numbers(a, b):
    return a + b

#2
def area_of_circle(radius):
    return math.pi * radius ** 2

#3
def add_all_numbers(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

#4
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

#5
def check_season(month):
    if month == 12:
        return "Winter"

#7
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return ["Not a quadratic equation"]

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return ["No real solution"]

    sqrt_disc = discriminant ** 0.5
    x1 = (-b - sqrt_disc) / (2*a)
    x2 = (-b + sqrt_disc) / (2*a)

    return [x1, x2]

print(solve_quadratic_eqn(1, 5, 1))

#8
def print_list(list):
    for item in list:
        print(item)

print_list([1, 2, 3, 4, 5])

