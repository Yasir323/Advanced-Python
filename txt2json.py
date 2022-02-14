# File to convert text to json file
import json

cities = []
with open('Top Cities.txt', 'r') as f:
    while line:= f.readline():
        cities.append(line.strip())

with open('topCities1000.json', 'w') as f:
    json.dump(cities, f, indent=4)