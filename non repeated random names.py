import random

list_a = ["Mike","Bob","June"]
list_b = ["Red","Green"]
list_c = ["Run","Jump"]

def user_generator():
    
    amount_of_names = int(input("how many names do you need?: "))

    list_so_far = []
    final_list = []

    for in amount_of_names:
        part_a = random.choice(list_a)
        part_b = random.choice(list_b)
        part_c = random.choice(list_c)
        temporary_name = (part_a, part_b, part_c)
        list_so_far.append(temporary_name)

    for i in list_so_far:
        if i not in final_list:
            final_list.append(i)
    
    print(final_list)


