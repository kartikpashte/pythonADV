import pandas as pd

data = pd.read_csv('data.csv')

# x = data["Calories"].mean()[0]
# x = data["Calories"].median()[0]
# x = data["Calories"].mode()[0]

data.fillna({"Calories":x}, inplace=True)

print(data)