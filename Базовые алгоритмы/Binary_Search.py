# Функция binary_search получает отсортированный массив и значение.
# Если значение присутствует в массиве, то функция возвращает его позицию


def binary_search(list, item):
    low = 0                 # Нижняя граница списка, в которой выполняется поиск
    high = len(list)-1      # Верхняя граница поиска

    while low <= high:      # Пока эта часть не сократится до одного элемента
        mid = (low + high)  # Проверяем средний элемент
        guess = list[mid]
        if guess == item:   # Значение найдено
            return mid
        if guess > item:    # Много
            high = mid -1
        else:               # Мало
            low = mid + 1
    return None             # Значения не существует


my_list = [1, 3, 5, 7, 9, 12, 14, 16, 18]

print(binary_search(my_list, 3))