import numpy as np
np.random.rand() # По умолчанию она генерирует число с плавающей точкой между 0 (включительно) и 1 (не включительно)


np.random.rand(5) # функция принимает в качестве аргументов через запятую целые числа, которые задают форму генерируемого массива. Например, получим массив из пяти случайных чисел:


# array([0.83745099, 0.58426808, 0.89206204, 0.41149807, 0.42445145])


# Массив из двух случайных строк и трёх столбцов:
np.random.rand(2, 3)
# array([[0.94931212, 0.06680018, 0.26707599],
#      [0.67908873, 0.18001743, 0.97732239]])


shape = (3, 4)
np.random.rand(*shape) # rand требует распаковки
# array([[0.66169176, 0.19455777, 0.06451088, 0.31919608],
#        [0.73536951, 0.67104408, 0.4762727 , 0.88153576],
#        [0.70672971, 0.96677145, 0.09273995, 0.86356465]])


shape = (2, 3)
np.random.sample(shape) # принимает форму массива в виде аргументов, перечисленных через запятую
# array([[0.39756103, 0.01995168, 0.2768951 ],
#       [0.82195372, 0.26435273, 0.00957881]])


# Первые два аргумента — нижняя и верхняя границы диапазона в формате float, третий опциональный аргумент — форма массива (если не задан, возвращается одно число). Форма массива задаётся кортежем или одним числом.

uniform(low=0.0, high=1.0, size=None)

# Получим пять чисел в интервале от 0.5 до 0.75:
np.random.uniform(0.5, 0.75, size=5)
# array([0.58078945, 0.58860342, 0.73790553, 0.63448265, 0.70920297])


# Получим массив из двух строк и трёх столбцов из чисел в интервале от -1000 до 500:
np.random.uniform(-1000, 500, size=(2, 3))
# array([[ 129.22164163,   77.69090611, -132.9656972 ],
#        [  18.65802226, -317.14793906,   85.3613547 ]])


# ГЕНЕРАЦИЯ INT

randint(low, high=None, size=None, dtype=int)

# Функцию randint нельзя запустить совсем без параметров, необходимо указать хотя бы одно число.

# Если указан только аргумент low, числа будут генерироваться от 0 до low-1, то есть верхняя граница не включается.
# Если задать low и high, числа будут генерироваться от low (включительно) до high (не включительно).
# size задаёт форму массива уже привычным для вас образом: одним числом — для одномерного или кортежем — для многомерного.
# dtype позволяет задать конкретный тип данных, который должен быть использован в массиве.
# Сгенерируем таблицу 2x3 от 0 до 3 включительно:

np.random.randint(4, size=(2,3))
# array([[3, 0, 1],
#       [2, 1, 3]])

# Чтобы задать и нижнюю, и верхнюю границы самостоятельно, передадим два числа, а затем форму:
np.random.randint(6, 12, size=(3,3))
# array([[ 9,  6, 10],
#        [10, 11, 10],
#        [ 7, 10, 11]])


# ГЕНЕРАЦИЯ ВЫБОРОК

# Функция random.shuffle перемешивает тот массив, к которому применяется, и возвращает None.
# Чтобы получить новый перемешанный массив, а исходный оставить без изменений, можно использовать функцию random.permutation.

playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
shuffled = np.random.permutation(playlist)
print(shuffled)
# ['The Beatles' 'Pink Floyd' 'Deep Purple' 'ACDC']
print(playlist)
# ['The Beatles', 'Pink Floyd', 'ACDC', 'Deep Purple']


np.random.permutation(10) # Перемешать набор чисел от 0 до n-1, где n — верхняя граница, которая бы использовалась для генерации набора чисел функцией arange.
# array([7, 8, 2, 9, 4, 3, 1, 0, 5, 6])


# Чтобы получить случайный набор объектов из массива, используется функция random.choice:
choice(a, size=None, replace=True)

# a — массив или число для генерации arange(a);
# size — желаемая форма массива (число для получения одномерного массива, кортеж — для многомерного; если параметр не задан, возвращается один объект);
# replace — параметр, задающий, могут ли элементы повторяться (по умолчанию могут).


# SEED ГЕНЕРАТОРА ПСЕВДОСЛУЧАЙНЫХ ЧИСЕЛ

np.random.seed(2021)

# В simple сохранте случайное число в диапазоне от 0 до 1
# simple = np.random.rand()
simple = np.random.sample()


# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их в переменную randoms
randoms = np.random.uniform(-150, 2021, size=120)


# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1, 101, size=(3,2))


# В переменную even сохраните четные числа от 2 до 16 (включительно)
even = np.arange(2,17,2)

# Перемешайте числа в even так, чтобы массив even изменился
np.random.shuffle(even)

# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, size=3, replace=False)

# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
