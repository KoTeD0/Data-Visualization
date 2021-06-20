from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice

dice_1 = Dice()
dice_2 = Dice(10)

results = []
for roll_num in range(50000):
    results.append(dice_1.roll() + dice_2.roll())

# Анализ результата
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result+1):
    frequencies.append(results.count(value))

# Визуализация результатов
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of Rolling D6 and D10 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')