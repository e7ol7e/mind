import math

def area(*args):
    n = len(args)
    is_right_trangle = False
    if n == 1:  # Круг
        return math.pi * args[0] ** 2

    if n == 2:  # Прямоугльник или квадрат
        return args[0] ** 2

    # Вычисление координат вершин используя длины сторон
    vertices = []
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = math.cos(angle) * args[i]
        y = math.sin(angle) * args[i]
        vertices.append((x, y))

    # Вычисление площади многоуглоника используя формулу площади Гаусса
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    return abs(area) / 2

def is_right_triangle(side1, side2, side3):
    return (lambda s: sum(x**2 for x in s[:2]) == s[2]**2)(sorted([side1, side2, side3]))


# Пример использования
def main():
    # Круг с радиусом 5
    circle_area = area(5)
    print("Площадь круга:", circle_area)

    # Квадрат со стороной 5
    rectangle_area = area(5, 5)
    print("Площадь прямоугольника:", rectangle_area)

    # Прямоугольный треугольник
    triangle_area = area(3, 4, 5)
    print(f"Площадь {["", "прямоугольного "][is_right_triangle(3, 4, 5)]}треугольника:", triangle_area)

    # Шестиугольник
    polygon_area = area(2, 3, 4, 5, 6, 7)
    print("Polygon area:", polygon_area)

if __name__ == "__main__":
    main()
