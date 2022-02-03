try:
    i = int(input('Enter a number:\t')) # Введите число
except ValueError as e:
    print('You entered a wrong number') # Вы ввели неправильное число
else:
    print(f'You entered {i}') # Вы ввели {i}
finally:
    print('Exit') # Выход из программы
    

# Какие минимальное и максимальное числа можно сохранить в битах?

import numpy as np

try:
    n = int(input('Введите кол-во бит:\t')) # Введите число
except ValueError as e:
    print('You entered a wrong number') # Вы ввели неправильное число


n_min = -(2**n)/2
n_max = (2**n)/2-1
print('Минимальное число: ', n_min)
print('Максимальное число', n_max)