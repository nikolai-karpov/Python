import numpy as np

arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True) # endpoint=False Последнее значение не включено


print('step: ', round(step,2))


print('ndim: ', arr.ndim)           # Размерность массива. Число осей, по которым возможна индексация 
print('size: ', arr.size)           # Узнайте число элементов массива.
print('shape: ', arr.shape)         # Форма массива
print('dtype: ', arr.dtype)         # Какой тип данных у элементов массива?
print('itemsize: ', arr.itemsize)   # Вес одного элемента в памяти


#arr = np.arange(8)
arr_new = arr.reshape((10, 6))
print(arr_new)
print(arr_new[::-1, -1]) # 1 - аргумент какие строки брать(: все строки), 2 - индекс в строке (: все столбцы)


# В переменную elem_5_3 сохраните элемент из 5 строки и 3 столбца:
elem_5_3 = mystery[4, 2]

# В переменную last сохраните элемент из последней строки последнего столбца
last = mystery[-1, -1]


# В переменную line_4 сохраните строку 4
line_4 = mystery[3]


# В переменную col_2 сохраните предпоследний столбец
col_2 = mystery[:, -2]


# Из строк 2-4 (включительно) получите столбцы 3-5 (включительно)
# Результат сохраните в переменную part
part = mystery[1:4, 2:5]


#  Сохраните в переменную rev последний столбец в обратном порядке
rev = mystery[::-1, -1]


# Сохраните в переменную trans транспонированный массив
trans = mystery.transpose()


# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)


# В переменную n_nan сохраните число пропущенных значений
n_nan = nans_index[nans_index==True].size


# Заполните пропущенные значения в массиве mystery нулями
mystery[np.isnan(mystery)] = 0


# Поменяйте тип данных в массиве mystery на int32
mystery = np.int32(mystery)


# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)


# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца.  

table = array.reshape((5, 3), order='F')  # order='F'порядок заполнения по столбцам


#  Сохраните в переменную col средний столбец из table
col = table[:, 1]
