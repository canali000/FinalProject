import pandas 

# data = pandas.read_csv("weather_data.csv")
# print(data.to_dict())


frame = {
    "day": {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    },
    "temp": {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
    "condition": {
        0: "Sunny",
        1: "Rain",
        2: "Rain",
        3: "Cloudy",
        4: "Sunny",
        5: "Sunny",
        6: "Sunny",
    },
}

data = pandas.DataFrame(frame)
a = data
a = data.temp.dtype
a = data.dtypes
a = data.columns
a = data.ndim
a = data.size
a = data.shape
a = data.values

a = data.head()
a = data.tail(3)
a = data.describe()
a = data.info()
a = data.max()
a = data.min()
a = data["temp"].std()
a = data.sample(3)
# x = data.set_index('temp', inplace=True)
# x = data.rename(columns={"temp": "Bedroom"}, inplace=True)



# a = data.dropna()
a = data["temp"]
a = data["temp"].count()
a = data["temp"].mean()
a = data["temp"].median()
a = data["temp"].value_counts()


a = data.groupby("temp")["day"].count() #index = temp

a = data["temp"]
a = data[["temp" , "day"]]
a = data[3:5]

a = data[data["temp"] > 15]
a = a.loc[4:5,["day","temp"]] # range select
a = a.iloc[0:7,[0,1]] # index select

a = data.iloc[0]  # First row of a data frame
# a = data.iloc[i]  # (i+1)th row
a = data.iloc[-1]  # Last row
a = data.iloc[:, 0]  # First column
a = data.iloc[:, -1]  # Last column
a = data.iloc[0:7]  # First 7 rows
a = data.iloc[:, 0:2]  # First 2 columns
a = data.iloc[1:3, 0:2]  # Second through third rows and first 2 columns
a = data.iloc[[0, 5], [1, 2]]  # 1st and 6th rows and 2nd and 3th columns

# iki noktaysa slice ayirma
# koseli parantezse index secme

# a = data.sort_values(by="temp")
# a.head()

a = data.sort_values(by=["temp", "day"], ascending=[False, False])
a.head(100)

a = data[data.isnull().any(axis=1)].head()

a = data[["temp", "day"]].agg(["min", "max"])
print(a)
