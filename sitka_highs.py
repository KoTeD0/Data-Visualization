import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    print(header_row)