import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# название заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=22)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# назначение размера шрифта делейний на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()
