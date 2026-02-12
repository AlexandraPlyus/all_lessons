import math


def square(side_a):
    area = (side_a ** 2)
    return math.ceil(area)


a = float(input("Сторона квадрата = "))
print(f"Площадь квадрата = {square(a)}")
