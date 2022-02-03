a = input('Введите число')

if isinstance(a, int):
    print('Переменная a является натуральным числом')
elif isinstance(a, float):
    print('Переменная a является дробным числом')
elif isinstance(a, str):
    print('Переменная a является строкой')
else:
    print('Неизвестный тип данных')