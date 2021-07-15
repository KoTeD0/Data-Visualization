import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/moscow_weather_2020-2021_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows, precipitations = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[header_row.index('DATE')], "%Y-%m-%d")
        try:
            high = float(row[header_row.index('TMAX')])
            low = float(row[header_row.index('TMIN')])
            precipitation = float(row[header_row.index('PRCP')])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            precipitations.append(precipitation)

# Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=1)
ax.plot(dates, lows, c='blue', alpha=1)
# ax.plot(dates, precipitations, c='cornflowerblue', alpha=1)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Форматирование диаграммы
title = f"Full Weather - 2020-2021\n{row[header_row.index('NAME')]}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# plt.savefig('moscow_weather_plot')
plt.show()
