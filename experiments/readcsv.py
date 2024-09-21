import csv
import time
# import os
import math

rads = math.radians(20)
print(rads)

print(time.strftime("%m.%d.%y"))
print(time.strftime("%A"))

with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))

print(data)
