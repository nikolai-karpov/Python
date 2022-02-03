# Функция должна получать на вход координаты двух точек (в виде четырёх чисел) и возвращать расстояние между ними.
# Чтобы посчитать расстояние между точками, нужно воспользоваться формулой:
# distance = sqrt((x1-x2)**2+(y1-y2)**2)

# Не забудьте проверить значения полученных аргументов!


def distance_between_dots(x1, x2, y1, y2):
    try:
        if (type(x1) or type(x2) or type(y1) or type(y2)) is not int or not float:
            raise ValueError
    except ValueError:
        print("Arguments are not numbers!")
        return

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**(1/2)
    return distance


print(distance_between_dots(1, 1, 2, 2))
print(distance_between_dots("a", 1, 2, 3))
