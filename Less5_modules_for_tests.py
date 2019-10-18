
def is_year_leap(a):
    """
    функция is_year_leap, принимающая 1 аргумент — год, и возвращающая True,
    если год високосный, и False иначе
    """
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_year_leap(int(input("Введите целое число: "))))


def triangle(a, b, c):
    """
    Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник
    с такими сторонами. Если треугольник существует, вернёт True, иначе False"""
    if (a + b > c) and (b + c > a) and (a + c > b):
        return True
    else:
        return False


if __name__ == "__main__":
    print(triangle(5, 4, 6))


def what_triangle(a, b, c):
    """
    Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник
    с такими сторонами и если существует, то возвращает тип треугольника Equilateral triangle (равносторонний),
    Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle)
    """
    if triangle(a, b, c) is True:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or a == c:
            return "Isosceles triangle "
        else:
            return "Versatile triangle "
    else:
        return "Not a triangle"


if __name__ == "__main__":
    print(what_triangle(7, 7, 2))

