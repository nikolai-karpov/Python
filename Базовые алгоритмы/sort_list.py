# Функция поиска наименьшего элемента массива
def find_smallest(arr):
    smallest = arr[0]               # для хранения наименьшего значения
    smallest_index = 0              # для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# Функция сортировки с выбором
def selection_sort(arr):                 # Сортируем массив
    newarr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)    # Находит наименьший элемент в массиве 
        newarr.append(arr.pop(smallest)) # и добавляет его в новый массив
    return newarr


print(selection_sort([5, 3, 6, 2, 10]))


# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:  
        return array                                    # Базовый случай: массивы с 0 и 1 элемент уже отсортированы
    else:
        pivot = array[0]                                # Рекурсивный случай
        less = [i for i in array[1:] if i <= pivot]     # Подмассив всех элементов меньших опорного
        greater = [i for i in array[1:] if i > pivot]   # Подмассив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)
    
    
print(quicksort([10, 5, 2, 3]))