import csv
from collections import Counter
from statistics import mean

import pandas


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     i = 0
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#
#     print(temperature)

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].tolist()
# print(temp_list)
# avg_temp = mean(temp_list)
# print(avg_temp)
# print(data[data.temp == data.temp.max()])

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dic = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]}

df = pandas.DataFrame(data_dic)
df.to_csv("color_count.csv")






