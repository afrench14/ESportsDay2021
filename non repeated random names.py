import random

list_a = ["Mike","Bob","June"]
list_b = ["Red","Green"]
list_c = ["Run","Jump"]

list_so_far = []

def user_generator():
    part_a = random.choice(list_a)
    part_b = random.choice(list_b)
    part_c = random.choice(list_c)

    temporary_name = (part_a, part_b, part_c)
    list_so_far.append(temporary_name)
