# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     i = 0
#     for row in data:
#         if i != 0:
#             temperatures.append(int(row[1]))
#         i += 1
#         print(row)
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

monday_temp_c = data[data.day == "Monday"].temp
monday_temp_f = (monday_temp_c * 1.8) + 32
print(monday_temp_f)

# Create a DataFrame from scracth
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv")
