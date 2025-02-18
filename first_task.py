# Задание 1.
# Написать программу, которая бы исследовала свойства платежной
# матрицы данной матричной игры.
# Входные данные − числа m и n, определяющие размеры платежной матрицы, и
# сама платежная матрица.
# Выходные данные − верхняя и нижняя цены игры, максиминные стратегии
# первого игрока и минимаксные стратегии второго игрока, седловые точки (если
# они есть) и цена игры в этом случае.


import numpy as np
import pandas as pd
def analyze_game_matrix(payoff_matrix):

    matrix_np = np.array(payoff_matrix)  # Преобразуем в NumPy массив для удобства
    rows, cols = matrix_np.shape

    # 1. Вычисление нижней цены игры (максимин)
    row_minima = np.min(matrix_np, axis=1)  # Находим минимумы в каждой строке
    lower_value = np.max(row_minima)  # Максимум из минимумов строк

    # 2. Вычисление верхней цены игры (минимакс)
    col_maxima = np.max(matrix_np, axis=0)  # Находим максимумы в каждом столбце
    upper_value = np.min(col_maxima)  # Минимум из максимумов столбцов

    # 3. Определение максиминной стратегии
    maximin_strategy = [(i + 1) for i in np.where(row_minima == lower_value)[0].tolist()]  # Номера строк, где достигается максимин (начиная с 1)

    # 4. Определение минимаксной стратегии
    minimax_strategy = [(j + 1) for j in np.where(col_maxima == upper_value)[0].tolist()]  # Номера столбцов, где достигается минимакс (начиная с 1)

    # 5. Поиск седловых точек
    saddle_points = []
    if lower_value == upper_value:
        # Ищем, где минимум в строке равен максимуму в столбце
        for i in range(rows):
            for j in range(cols):
                if matrix_np[i, j] == lower_value and matrix_np[i, j] == row_minima[i] and matrix_np[i, j] == col_maxima[j]:
                    saddle_points.append((i + 1, j + 1))  # Номера строк и столбцов, начиная с 1
        game_value = lower_value  # Цена игры равна верхней/нижней цене
    else:
        game_value = None  # Седловой точки нет

    return upper_value, lower_value, maximin_strategy, minimax_strategy, saddle_points, game_value

def get_matrix_from_input():

    while True:
        try:
            m = int(input("Введите количество строк (m): "))
            n = int(input("Введите количество столбцов (n): "))
            if m <= 0 or n <= 0:
                print("Размеры матрицы должны быть положительными целыми числами.")
                continue
            break  # Выход из цикла, если ввод корректен
        except ValueError:
            print("Ошибка: Введите целые числа для размеров матрицы.")

    print("Введите элементы матрицы построчно, разделяя числа пробелами:")
    matrix = []
    for i in range(m):
        while True:
            try:
                row_str = input(f"Введите строку {i+1}: ")
                row = [float(x) for x in row_str.split()]  # Преобразуем введенную строку в список чисел
                if len(row) != n:
                    print(f"Ошибка: В строке должно быть {n} элементов. Попробуйте еще раз.")
                    continue
                matrix.append(row)
                break  # Выход из цикла, если строка введена корректно
            except ValueError:
                print("Ошибка: Введите числа, разделенные пробелами.")
    return matrix

# Примеры платежных матриц для тестирования (из задания)
payoff_matrix_1 = [
    [2, 4, 1, 5],
    [1, -1, 3, 2],
    [5, 2, -4, 0],
    [-2, 5, -3, -4]
]

payoff_matrix_2 = [
    [2, 3, -1, 4],
    [3, 2, 4, 1],
    [-4, 3, -1, -2],
    [-5, 5, -3, -4]
]

payoff_matrix_3 = [
    [2, 2, 6, 5],
    [3, 3, 7, 7],
    [4, 3, 4, 2],
    [5, 6, 2, 4]
]

payoff_matrix_4 = [
    [0.5, 0.3, 0.6, 0.7, 0.8],
    [0.6, 0.2, 0.4, 0.9, 1.0],
    [0.7, 0.4, 0.7, 1.2, 0.9],
    [1.1, 0.6, 0.5, 1.0, 0.6],
    [0.3, 0.5, 0.9, 0.7, 1.0],
    [1.2, 0.4, 0.3, 0.2, 0.6]
]

payoff_matrix_5 = [
    [4, 5, 6, 7],
    [2, 3, 4, 5],
    [7, 6, 8, 10],
    [8, 5, 3, 7]
]

payoff_matrix_6 = [
    [4, 5, 6, 7, 10],
    [9, 3, 6, 5, 7],
    [7, 6, 8, 11, 10],
    [8, 5, 4, 7, 4]
]

matrix_examples = {
    1: payoff_matrix_1,
    2: payoff_matrix_2,
    3: payoff_matrix_3,
    4: payoff_matrix_4,
    5: payoff_matrix_5,
    6: payoff_matrix_6
}

# Выводим примеры матриц
print("Примеры платежных матриц:")
for i in range(1, 7):
    print(f"Матрица {i}:")
    for row in matrix_examples[i]:
        print(row)
    print("-" * 10)

while True:
    choice = input("Использовать пример матрицы (1-6) или ввести свою (в)? ").lower()
    if choice in ['1', '2', '3', '4', '5', '6']:
        matrix_index = int(choice) - 1
        selected_matrix = [payoff_matrix_1, payoff_matrix_2, payoff_matrix_3, payoff_matrix_4, payoff_matrix_5, payoff_matrix_6][matrix_index]
        break
    elif choice == 'в':
        selected_matrix = get_matrix_from_input()
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите число от 1 до 6 или 'в'.")

# Анализируем выбранную матрицу и выводим результаты
upper_value, lower_value, maximin_strategy, minimax_strategy, saddle_points, game_value = analyze_game_matrix(selected_matrix)

print("\nРезультаты анализа:")
print(f"  Верхняя цена игры: {upper_value}")
print(f"  Нижняя цена игры: {lower_value}")
print(f"  Максиминная стратегия (строки): {', '.join(map(str, maximin_strategy))}")
print(f"  Минимаксная стратегия (столбцы): {', '.join(map(str, minimax_strategy))}")

if saddle_points:
    print(f"  Седловые точки: {saddle_points}")
    print(f"  Цена игры: {game_value}")
else:
    print("  Седловые точки отсутствуют.")
    print("  Цена игры не определена (необходимо смешанное расширение).")

print("-" * 30)
