# with open("weather_data.csv", mode="r", encoding="utf-8") as dataFile:
#     data = dataFile.readlines()

# print(data)

# import csv

# with open("weather_data.csv", mode="r", encoding="utf-8") as dataFile:
#     data = csv.reader(dataFile)
#     temperatures = []

#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

dictData = data.to_dict() 
print(dictData)

listData = data["temp"].to_list()
print(listData)
avg = sum(listData)/len(listData)
print(avg)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp = monday.temp
fah = temp * 1.8 + 32
print(fah)

# cel 0 +100 100
# fah 32 +180 212
# (C - 0)/100 = (F - 32) / 180
# C * 1.8 + 32 = F

dictData = {
    "students" : ["Can", "Ali", "Bilgin"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(dictData)

print(data.to_csv("newData.csv"))
