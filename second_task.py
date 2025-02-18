# Задание 2.
# Построить платежную матрицу игры, найти ее верхнюю и нижнюю
# цены игры и там, где это возможно, седловую точку и значение выигрыша
#
# Каждый из двух участников игры, независимо один от другого,
# показывает на руке «камень», «бумагу» или «ножницы», при
# этом «бумага» выигрывает у «камня» одно очко, «камень
# выигрывает» у «ножниц» два очка, «ножницы» выигрывают у
# «бумаги» три очка.



import numpy as np
import pandas as pd


def analyze_rock_paper_scissors_game():


    # Построение платежной матрицы
    payoff_matrix = np.array([
        [0, -1, 2],
        [1, 0, -3],
        [-2, 3, 0]
    ])

    # Вычисление нижней цены игры (maximin)
    row_minima = np.min(payoff_matrix, axis=1)
    lower_value = np.max(row_minima)

    # Вычисление верхней цены игры (minimax)
    col_maxima = np.max(payoff_matrix, axis=0)
    upper_value = np.min(col_maxima)

    # Поиск седловой точки
    if lower_value == upper_value:
        saddle_point_row, saddle_point_col = np.where(payoff_matrix == lower_value)
        saddle_point = (saddle_point_row[0] + 1, saddle_point_col[0] + 1)
        game_value = lower_value
        print(f"Седловая точка найдена: строка {saddle_point[0]}, столбец {saddle_point[1]}")
        print(f"Цена игры (выигрыш игрока A): {game_value} очков")
    else:
        saddle_point = None
        game_value = None
        print("Седловая точка не найдена. Необходимы смешанные стратегии.")
        print(f"Верхняя цена игры: {upper_value} очков")
        print(f"Нижняя цена игры: {lower_value} очков")

    index = ["Камень", "Бумага", "Ножницы"]
    columns = ["Камень", "Бумага", "Ножницы"]
    df = pd.DataFrame(payoff_matrix, index=index, columns=columns)
    print("\nПлатежная матрица:")
    print(df)


analyze_rock_paper_scissors_game()