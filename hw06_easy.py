# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math


class Triangle:
    x1 = 2
    y1 = -3
    x2 = 1
    y2 = 1
    x3 = -6
    y3 = 5

    def area(self):
        return 1 / 2 * math.fabs((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3))

    def height(self):
        return math.fabs((self.y2 - self.y3) * self.x1 + (self.x3 - self.x2) * self.y1 + (self.x2 * self.y3 - self.x3 * self.y2)) / math.sqrt((self.y2 - self.y3) ** 2 + (self.x3 - self.x2) ** 2)

    def perimeter(self):
        ab = math.sqrt(math.sqrt(math.fabs(self.x1 - self.x2)) + math.sqrt(math.fabs(self.y1 - self.y2)))
        bc = math.sqrt(math.sqrt(math.fabs(self.x2 - self.x3)) + math.sqrt(math.fabs(self.y2 - self.y3)))
        ac = math.sqrt(math.sqrt(math.fabs(self.x1 - self.x3)) + math.sqrt(math.fabs(self.y1 - self.y3)))
        return ab + bc + ac

triangle1 = Triangle()
print(triangle1.area())
print(triangle1.height())
print(triangle1.perimeter())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezium:
    x1 = 1
    y1 = 2
    x2 = 3
    y2 = 7
    x3 = 7
    y3 = 7
    x4 = 9
    y4 = 2

    def istrapezium(self):
        return math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) == math.sqrt((self.x4 - self.x2) ** 2 + (self.y4 - self.y2) ** 2)

    def side_ab(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def side_bc(self):
        return math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)

    def side_cd(self):
        return math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)

    def side_da(self):
        return math.sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)

    def fd(self):
        return (self.side_da() + self.side_bc()) / 2

    def bf(self):
        return math.sqrt(math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1)) ** 2 - self.fd())

    def perimeter(self):
        return self.side_ab() + self.side_bc() + self.side_cd() + self.side_da()

    def area(self):
        return ((self.side_da() + self.side_bc()) / 2) * self.bf()


trapezium1 = Trapezium()
print(trapezium1.istrapezium())
print(trapezium1.side_ab())
print(trapezium1.side_bc())
print(trapezium1.side_cd())
print(trapezium1.side_da())
print(trapezium1.perimeter())
print(trapezium1.area())
