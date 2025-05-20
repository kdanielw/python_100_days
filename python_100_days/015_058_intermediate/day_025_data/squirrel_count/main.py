import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_colors = data["Primary Fur Color"].dropna().unique().tolist()
squirrel_quantity = data["Primary Fur Color"].dropna().value_counts().tolist()
print(squirrel_colors)
print(squirrel_quantity)

squirrel_colors_dict = {
    "Fur Color": squirrel_colors,
    "Count": squirrel_quantity
}

squirrel_count = pandas.DataFrame(squirrel_colors_dict)
squirrel_count.to_csv("squirrel_count.csv")