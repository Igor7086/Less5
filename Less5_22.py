from math import sqrt


class MyArea:
    """Прямоугольная площадка (свойства: две стороны)
    """
    def __init__(self, side_one, side_two):
        self.side_one = side_one
        self.side_two = side_two

    def square(self):
        """вычисляем площадь"""
        return self.side_one * self.side_two

    def perimeter(self):
        """вычисляем периметр"""
        return self.side_one * 2 + self.side_two * 2

    def __str__(self):
        return "Для прямоугольника со сторонами {} и {} площадь: {}, периметр: {} ".format(self.side_one, self.side_two,
                                                                                          self.square(),
                                                                                           self.perimeter())


if __name__ == "__main__":
    num1 = MyArea(23, 34)
    print(num1)


class PointsMap:
    """расстояние между точками или до начала координат"""

    def __init__(self, x1, y1, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance_xy(self):
        return sqrt((self.x2 - self.x1)**2 +(self.y2 - self.y1)**2)

    def __str__(self):
        if self.x2 == 0 and self.y2 == 0:
            return "Расстояние от точки ({}, {}) до начала координат: {}".format(self.x1, self.y1, self.distance_xy())
        else:
            return "Расстояние от точки ({}, {}) до точки ({}, {}): {}".format(self.x1, self.y1, self.x2, self.y2,
                                                                               self.distance_xy())


if __name__ == "__main__":
    num1 = PointsMap(2, 4)
    print(num1)

