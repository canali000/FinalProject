import pandas

data = pandas.read_csv("help/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240603.csv")

redRow = data[data["Primary Fur Color"] == "Cinnamon"]
redFur = len(redRow["Primary Fur Color"])
# redFur = redRow["Primary Fur Color"].size

grayRow = data[data["Primary Fur Color"] == "Gray"]
grayFur = grayRow["Primary Fur Color"].size

blackRow = data[data["Primary Fur Color"] == "Black"]
blackFur = blackRow["Primary Fur Color"].size


dictData = {
    "Fur Color" : ["gray", "red", "black"],
    "Count" : [grayFur,redFur,blackFur]
}

pandas.DataFrame(dictData).to_csv("sqCount.csv")

# print(data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].size)

furdata = data.groupby(["Primary Fur Color"]).head(5)
# print(furdata)
