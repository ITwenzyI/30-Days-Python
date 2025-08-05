# Day 14 - Higher Order Functions
from functools import reduce

#1
# | Funktion   | Zweck                                                     | Rückgabe                                  |
# | ---------- | --------------------------------------------------------- | ----------------------------------------- |
# | `map()`    | Wendet eine Funktion auf **alle Elemente** an             | Neuer Iterator mit Ergebnissen            |
# | `filter()` | Gibt **nur Elemente zurück**, die eine Bedingung erfüllen | Neuer Iterator mit „gefilterten“ Werten   |
# | `reduce()` | Kombiniert **alle Werte zu einem einzigen Ergebnis**      | Ein einzelner Wert (z.B. Summe, Produkt) |
#

#2
# Higher-Order Function = Eine Funktion, die eine andere Funktion entgegennimmt oder zurückgibt.
# Closure = Eine Funktion, die auf Variablen außerhalb ihres Gültigkeitsbereichs zugreifen kann, auch nachdem der äußere Funktionskontext abgeschlossen ist.

# Decorator = Ein Wrapper um eine Funktion, der ihr Verhalten erweitert – z.B. Logging, Caching, etc.
# def decorator(fn):
#     def wrapper():
#         print("Vorher")
#         fn()
#         print("Nachher")
#     return wrapper
#
# @decorator # @decorator ist Kurzform für say_hi = decorator(say_hi)
# def say_hi():
#     print("Hi!")
#
# say_hi()

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Level 2
#3

def change_upper(name):
    return name.upper()

upper_list = map(change_upper, countries)
print(list(upper_list))

#2
square_number = map(lambda x: x ** 2, numbers)
print(list(square_number))

#3
upper_name = map(change_upper, names)
print(list(upper_name))

#4
def check_country(country):
        if "land" in country:
            return True
        else:
            return False


filter_country = filter(check_country, countries)
print(list(filter_country))

#5
def six_countries(country):
    if len(country) == 6:
        return True
    else:
        return False

filter_six_countries = filter(six_countries, countries)
print(list(filter_six_countries))

#6
def six_more_countries(country):
    if len(country) >= 6:
        return True
    else:
        return False

filter_six_more_countries = filter(six_more_countries, countries)
print(list(filter_six_more_countries))

#7
def e_start_country(country):
    if country.startswith("E"): # if "E" in country:
        return True
    else:
        return False

e_start_country = filter(e_start_country, countries)
print(list(e_start_country))

#8
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda x, y: x*y, filter(lambda x: x % 2, map(lambda x: x ** 2, nums)))
print(result)

#9
def get_string_list(listt):
    return list(map(lambda x: str(x), listt))
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_string_list(test))

#10
sum = reduce(lambda x, y: x + y, numbers)#
print(sum)

#11
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def reducer(acc, country):
    return acc + ', ' + country

sentence = reduce(reducer, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries'

print(sentence)
