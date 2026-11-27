import pandas as kartik

# data = {
#     "cars" : ["BMW","TATA","HONDA"],
#     "passing":[2010,2020,2019]
# }

# mydata = kartik.DataFrame(data)

# print(mydata.to_string(index=False))

# print(kartik.__version__)

# data = [1,3,2,5,4,6]

# mydata = kartik.Series(data,index = ["a","b","c","d","e","f"])

# print(mydata)


# calories = {"day1": 420, "day2": 380, "day3": 390}

# data = kartik.Series(calories,index = ["day1","day2"])

# print(data)

# data = {
  # "calories": [420, 380, 390, 450, 410, 370, 430, 460, 395, 440, 385, 415, 470, 400, 425],
  # "duration": [50, 40, 45, 55, 48, 38, 52, 60, 42, 54, 41, 47, 58, 44, 50]
# }

# mydata = kartik.DataFrame(data)
# print(mydata.to_string(index=False))


storage = {
  "ram": [2,4,6,8,12,24,],
  "rom": [32,64,128,256,512,1080]
}
mydata = kartik.DataFrame(storage)
print(mydata.to_string(index=False))

storage = {
  "ram": [2,4,6,8,12,24,],
  "rom": [32,64,128,256,512,1080]
}
mydata = kartik.DataFrame(storage)
print(mydata)