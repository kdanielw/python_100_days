# List Comprehension
numbers = [1, 2, 3]
new_numbers = [n +1 for n in numbers]
print(new_numbers)

test_range = range(1, 5)
list_range = [n * 2 for n in test_range]
print(list_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

upper_names = [name.upper() for name in names if len(name) >= 5]
print(upper_names)

# Dictionary Comprehension
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students = {name:random.randint(0,100) for name in names}
print(students)
passed_students = {name:score for (name, score) in students.items() if score >= 70}
print(passed_students)

# Looping through dicitionaries
students = {
    "student": ["Angela", "Daniel", "Stahma"],
    "score": [10, 7, 9]
}

for (key, value) in students.items():
    print(key)

# Looping through dataframes
import pandas

students_data_frame = pandas.DataFrame(students)
for (key, value) in students_data_frame.items():
    print(value)

# Looping through rows of a dataframe
for (index, row) in students_data_frame.iterrows():
    print(row.student)