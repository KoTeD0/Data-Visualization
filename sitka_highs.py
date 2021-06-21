import csv

from matplotlib import pyplot as plt


def makeCelsium(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    # Чтение максимальных температур
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(makeCelsium(high))

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Форматирование диаграммы
plt.title("Daily High temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()