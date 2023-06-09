# Задание 1.
# Создать класс TrafficLight (светофор)
# и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
# В рамках метода running реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный)
# составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.
# Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# from time import sleep

# class TrafficLight:

#     def __init__(self, colour):
#         self.__colour = colour
#         print("СВЕТОФОР ВКЛЮЧЕН")

#     def running(self):
#         for key, volues in self.__colour.items():
#             print(f"горит {key} время ожидания {volues} сек")
#             sleep(volues)

# traf = TrafficLight(colour={
#     "КРАСНЫЙ": 7,
#     "ЖЕЛТЫЙ": 2,
#     "ЗЕЛЕНЫЙ": 3})

# traf.running()
# print("СВЕТОФОР ВЫКЛЮЧЕН")

# Задание 2.
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

# class Road:
#     _weight: float = 0.025 # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см (взято из сети)

#     def __init__(self, length, width):
#         self._lenght = length
#         self._width = width
        
#         print(f'Дорога имеет длину {self._lenght} метров и ширину {self._width} метров')

#     def road_weight(self, thickness):
#          weighing_result = self._lenght * self._width * thickness * self._weight
#          print(f'Вес асфальта, требуемый для укладки дороги толщиной {thickness} см, равен {weighing_result} т')



# # r1 = Road(10000, 5)
# # w1 = r1.road_weight(10)

# road_area = Road(1000, 10)
# weigth_road = road_area.road_weight(20)


# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.

# class Worker:

#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
        
#         self._income = {"wage": wage, "bonus": bonus}

# class Position(Worker):

#     def get_full_name(self):
    
#         return self.name + " " + self.surname

#     def get_total_income(self):
#         return self._income.get("wage") + self._income.get("bonus")
    
#     def string(self):
#         return self.get_full_name() + " " + self.position \
# + " доход " + str(self.get_total_income())


# w1 = Position("Петр", "Петров", "суперпрограммист", 12000, 3000)
# print(end="\n")
# print(f"{w1.surname} {w1.name} {w1.position} доход с бонусом {w1.get_total_income()}$ ")
# print(w1.string())

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

# class Matrix():

#     def __init__(self, list_1):
#         self.list_1 = list_1
#         self.row_count = len(list_1)
#         self.col_count = len(list_1[0])

#     def __str__(self):
#         ret_val = ""
#         for i in range(self.row_count):
#             for j in range(self.col_count):
#                 ret_val +=  str(self.list_1[i][j]) + " "
#             ret_val += '\n'

#         return ret_val

#     def get_item(self, row, col):
#         try:
#             ret_val = self.list_1[row][col]
#         except:
#             ret_val = 0

#         return ret_val

#     def __add__(self, other):

#         new_list_1 = []
#         max_rows = max(self.row_count, other.row_count)
#         max_cols = max(self.col_count, other.col_count)

#         for i in range(max_rows):
#             new_list_1.append([])
#             for j in range(max_cols):
#                 new_list_1[i].append(self.get_item(i, j) + other.get_item(i, j))

#         return Matrix(new_list_1)


# m1 = Matrix([[30, 15], [32, 44]])
# print(f"Перавя матрица \n{m1}")

# m2 = Matrix([[97, 20], [29, 76]])
# print(f"Вторая матрица \n{m2}")

# m3 = m1 + m2
# print(f"Итоговая матрица \n{m3}")

# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько 
# легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке
# Пример:
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# c = input("Введите что поет Винни-Пух:  ")
# st = c.split()

# f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
# t = f(st[0])
# if all([f(i) == t for i in st]):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')