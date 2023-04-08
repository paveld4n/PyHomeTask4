# Задание 4.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init())
# , который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных 
# в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86

# 3 5 32
# 2 4 6
# -1 64 -8

# 3 5 8 3
# 8 3 7 1

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов 
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой 
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix():

    def __init__(self, list_1):
        self.list_1 = list_1
        self.row_count = len(list_1)
        self.col_count = len(list_1[0])

    def __str__(self):
        ret_val = ""
        for i in range(self.row_count):
            for j in range(self.col_count):
                ret_val +=  str(self.list_1[i][j]) + " "
            ret_val += '\n'

        return ret_val

    def get_item(self, row, col):
        try:
            ret_val = self.list_1[row][col]
        except:
            ret_val = 0

        return ret_val

    def __add__(self, other):

        new_list_1 = []
        max_rows = max(self.row_count, other.row_count)
        max_cols = max(self.col_count, other.col_count)

        for i in range(max_rows):
            new_list_1.append([])
            for j in range(max_cols):
                new_list_1[i].append(self.get_item(i, j) + other.get_item(i, j))

        return Matrix(new_list_1)


m1 = Matrix([[30, 15], [32, 44]])
print(f"Перавя матрица \n{m1}")

m2 = Matrix([[97, 20], [29, 76]])
print(f"Вторая матрица \n{m2}")

m3 = m1 + m2
print(f"Итоговая матрица \n{m3}")
