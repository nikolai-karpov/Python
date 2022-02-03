"""Игра угадай число
Компьютер сам загадывает и сам угадывает число"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число
    Args:
        number (int. optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)      # Предпалагаемое число
        if predict_number == number:
            break                                       # Выход из цикла, если угадали
    return (count)


def score_game(random_predict) -> int:
    """[За какое кол-во попыток в среднем угадываем]за 1000 подходов

    Args:
        random_predict ([type]): [Функция угадывания]

    Returns:
        int: [Среднее кол-во попыток]
    """
    
    count_ls = []                                           # Список в который сохраняем кол-во попыток
    np.random.seed(1)                                       # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))   # Высчитаваем средний показатель за 1000 запусков

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))                          # Вычисляем среднее значение в счетчике
    print(f'Ваш алгоритм в реднем угадывает за {score} попыток')
    return(score)

        
# RUN
score_game(random_predict)

