class NonNegative:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, param, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        param.__dict__[self.my_attr] = value

    # def __set_name__(self, owner, my_attr):
    # #     # owner - владелец атрибута - <class '__main__.Worker'>
    # #     # my_attr - имя атрибута владельца - hours, rate
    #     self.my_attr = my_attr
class Defence_age:
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, var, value):
        if value < 18:
            raise ValueError("Возраст может быть менее 18 лет")
        var.__dict__[self.my_attr] = value

class Worker:
    # имя атрибута, который делаем дескриптором, в конструктор не передаем
    hours = NonNegative("hours")
    rate = NonNegative("rate")
    age = Defence_age("age")

    def __init__(self, name, surname, hours, rate, age):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate
        self.age = age

    def total_profit(self):
        return self.hours * self.rate

s1 = Worker('Иван', 'Иванов', 10, 100, 100)
print(s1.total_profit())

# OBJ.hours = 10
# OBJ.rate = 100
# print(OBJ.total_profit())
