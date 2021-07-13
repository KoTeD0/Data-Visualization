import csv

from matplotlib import pyplot as plt
from datetime import datetime


def makeCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    # Чтение максимальных температур
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        highs.append(makeCelsius(high))
        dates.append(current_date)
        lows.append(makeCelsius(low))

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=1)
ax.plot(dates, lows, c='blue', alpha=1)
plt.fill_between(dates, highs, lows, facecolor='aqua', alpha=0.1)

# Форматирование диаграммы
plt.title("Daily High and Low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
