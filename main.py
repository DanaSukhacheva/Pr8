class Soda:                                                          #1
    def __init__(self, additive = None):
        self.additive = additive
    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print("Обычная газировка")

drink1 = Soda("syrup")
drink1.show_my_drink()

drink2 = Soda()
drink2.show_my_drink()





class TriangleChecker:                                      #2
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

    def is_triangle(self):
        if not all(isinstance(side, (int, float)) for side in self.sides):      #isinstance проверка принадлежит ли к определенному класу или типу данных
            return "Нужно вводить только числа!"
        if any(sides <= 0 for sides in self.sides ):
            return "С отрицательными числами ничего не выйдет!"
        a, b, c = self.sides
        if a+b >c and a+c> b and c+b>a:
            return "Ура, можно построить треугольник!"
        else: return "Жаль, но из этого треугольник не сделать."
triangle1 = TriangleChecker(3,4,5)
print(triangle1.is_triangle())
triangle2 = TriangleChecker(-1,2,3)
print(triangle2.is_triangle())
triangle3 = TriangleChecker(1,2,"four")
print(triangle3.is_triangle())
triangle4 = TriangleChecker(1,2,3)
print(triangle4.is_triangle())



class KgToPounds:                          #3
    def __init__(self, kg):
        self._kg = kg
    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, value):
        self._kg = value

    def to_pounds(self):
        return self.kg * 2.205

weight = KgToPounds(10)
print(weight.kg)
print(weight.to_pounds())

weight.kg = 20
print(weight.kg)
print(weight.to_pounds())

class Nikola:                                      #4
    __slots__ = ['name', 'age']   #ограничивание количества атрибутов добавляемых в класс
    def __init__(self, name, age):
        if name != "Николай":
            self.name = f"Я не {name}, а Николай"
        else:
            self.name = name
        self.age = age

person1 = Nikola("Максим", 30)
print(person1.name)
print(person1.age)
person2 = Nikola("Николоай", 40)
print(person2.name)
print(person2.age)




class RealString:                                    #5
    def __init__(self, value):
        self.value = value

    def __len__(self):
        return len(self.value)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)


str1 = RealString("Apple")
str2 = RealString("Яблоко")

print(str1 > str2)
print(str1 < str2)
print(str1 > "Banana")



