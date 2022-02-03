# Вычисление среднее арифметического значений списка.
# Не забудьте проверить значение полученного аргумента!
# arithmetic_mean = lambda list_numbers: sum(list_numbers) / len(list_numbers)


def arithmetic_mean(list_numbers):
    try:
        if type(list_numbers) is not list:
            raise ValueError("You should pass list to this function!")
    except ValueError as err:
        print(err)
        return
    try:
        average = sum(list_numbers) / len(list_numbers)
    except TypeError:
        print("List should contain numbers!")
        return
    return average


print(arithmetic_mean([1, 2, 3]))
print(arithmetic_mean(1))
print(arithmetic_mean(["a", 1]))
