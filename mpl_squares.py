import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values ,squares, linewidth=3)

# название заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=22)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# назначение размера шрифта делейний на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()