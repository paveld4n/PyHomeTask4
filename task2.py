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

class Road:
    __weight = 0.025 # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см (взято из сети. Значение не изменяется)

    def __init__(self, length, width):
        self._lenght = length
        self._width = width
        
        print(f'Дорога имеет длину {self._lenght} метров и ширину {self._width} метров')

    def road_weight(self, thickness):
         weighing_result = self._lenght * self._width * thickness * self.__weight
         print(f'Вес асфальта, требуемый для укладки дороги толщиной {thickness} см, равен {weighing_result} т')



# r1 = Road(10000, 5)
# w1 = r1.road_weight(10)

road_area = Road(1000, 10)
weigth_road = road_area.road_weight(20)