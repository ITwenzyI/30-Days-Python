# Day 12 - Modules
# import ...
# from ... import ...
from random import randint
import string

def random_user_id():
    user_id = ""
    for i in range(6):
        x = randint(1, 3)
        if x == 1:
            str = string.ascii_lowercase
            y = randint(0, 25)
            user_id = user_id + str[y]
        elif x == 2:
            str = string.digits
            y = randint(0, 9)
            user_id = user_id + str[y]
        else:
            str = string.ascii_uppercase
            y = randint(0, 25)
            user_id = user_id + str[y]
    return user_id

def user_id_gen_by_user():
    length = int(input("Enter the length of user_id : "))
    amount = int(input("Enter the amount of user_id : "))
    user_ids = []
    user_id = ""
    for i in range(amount):
        for j in range(length):
            x = randint(1, 3)
            if x == 1:
                str = string.ascii_lowercase
                y = randint(0, 25)
                user_id = user_id + str[y]
            elif x == 2:
                str = string.digits
                y = randint(0, 9)
                user_id = user_id + str[y]
            else:
                str = string.ascii_uppercase
                y = randint(0, 25)
                user_id = user_id + str[y]
        user_ids.append(user_id)
        user_id = ""
    return user_ids


def rgb_color_gen():
    rgb_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    str_rgb_color = str(rgb_color)
    return "rgb" + str_rgb_color






