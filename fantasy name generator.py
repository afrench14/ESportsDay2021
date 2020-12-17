import csv
import random

'''
count = 1
number_of_names = int(input("how many random names would you like to generate?: "))

def random_name_generator():
    with open("nicknamesList1.csv") as file_1:
        name_list_1 = file_1.read().split()
        name_part_1 = random.choice(name_list_1)

    with open("nicknamesList2.csv") as file_2:
        name_list_2 = file_2.read().split()
        name_part_2 = random.choice(name_list_2)

    with open("nicknamesList3.csv") as file_3:
        name_list_3 = file_3.read().split()
        name_part_3 = random.choice(name_list_3)

    print("your random nickname is:  ", name_part_1, name_part_2, name_part_3)

while count < number_of_names:
    random_name_generator()
    count = count + 1
'''

#opening the first file into a list then closing it again
first_file = open("nicknamesList1.csv", "r", newline = "")
file_reader_1 = csv.reader(first_file)
for row in file_reader_1:
    first_name = row.strip("/n")
    first_name_list.append(first_name)
first_file.close()

#opening the second file into a list then closing it again
second_file = open("nicknamesList2.csv", "r", newline = "")
file_reader_2 = csv.reader(second_file)
for row in file_reader_2:
    second_name = row.strip("/n")
    second_name_list.append(second_name)
second_file.close()

#opening the third file into a list then closing it again
third_file = open("nicknamesList3.csv", "r", newline = "")
file_reader_3 = csv.reader(third_file)
for row in file_reader_3:
    third_name = row.strip("/n")
    third_name_list.append(third_name)
third_file.close()

#opening an empty list to write the names to
names = []

#creating the names and writing them to the list, then printing the list
for idx1 in range(0, len(first_name_list)):
    for idx2 in range(0, len(second_name_list)):
        for idx3 in range(0, len(third_name_list)):
            names.append(first_name_list[idx1] + "-" + second_name_list[idx2] + "-" + third_name_list[idx3])

print(names)
