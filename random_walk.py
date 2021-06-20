from random import choice

class RandomWalk:
    """Класс для генерирования случайных блужданий"""

    def __init__(self, num_points=5000):
        """Инициалиирует атрибуты блужданий"""
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Определение направления и длинны перемещения:
        x_direction = choice([-1, 1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([-1, 1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance

        # Отклонение нулевых перемещений
        if x_step == 0 and y_step == 0:
            self.get_step()
        return x_step, y_step

    def fill_walk(self):
        """Вычисляет все точки блужданий"""

        # Шаги генерируются до достижения нужной длинны
        while len(self.x_values) < self.num_points:

            next_step = self.get_step()

            # вычисление следующих значений x и y
            x = self.x_values[-1] + next_step[0]
            y = self.y_values[-1] + next_step[1]

            self.x_values.append(x)
            self.y_values.append(y)