import numpy as np
from datetime import datetime


# Делаем массив int'ов
# Делаем 4 подмассива
# Далаем из них матрицу и возвращаем её
def get_matrix(str):
    arr = np.array(list(map(int, str)))
    separated_arr = np.split(arr, 4)
    matrix = np.matrix(separated_arr)
    return matrix


# Из матрицы получаем диагональ
# Первое и второе число диагонали - день, третье и четвертое - месяц.
# Находим определитель матрицы, его модуль и целочисленное деление на 100
# И в сочетании с "1900" получаем год в 20ом веке
# Сразу завертываем все полученные данные в дататайм и выводим
def get_date(mtrx):
    diag = np.diag(mtrx)
    day = str(diag[0]) + str(diag[1])
    month = str(diag[2]) + str(diag[3])

    det = int(round(np.linalg.det(mtrx), 0))
    year = 1900 + (abs(det) % 100)

    date = datetime(year, int(month), int(day))
    return date


mtrx = get_matrix(input())                      # Получаем матрицу
date = get_date(mtrx)                           # Из матрицы получаем дату
print(datetime.strftime(date, "%d %b %Y"))      # Выводим в красивом виде
