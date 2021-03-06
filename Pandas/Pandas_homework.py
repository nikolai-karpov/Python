import pandas as pd


melb_data = pd.read_csv('data/melb_data.csv', sep=',')

print('цена объекта недвижимости под индексом 15', melb_data.loc[15, 'Price'])


print('объект под индексом 90 был продан', melb_data.loc[90, 'Date'])


print('площадь участка, на котором находится здание с индексом 3521', melb_data.loc[3521, 'Landsize'])
print('площадь участка, на котором находится здание с индексом 1690', melb_data.loc[1690, 'Landsize'])

dif_size = melb_data.loc[3521, 'Landsize'] / melb_data.loc[1690, 'Landsize']
print('площадь участка с индексом 3521, больше площади участка с индексом 1690 в', round(dif_size), 'раз')


# Выведем первые пять строк нашей таблицы:
print(melb_data.head())


# Следующий код выведет семь последних строк нашей таблицы:
print(melb_data.tail(7))


# с помощью атрибута shape, возвращаем кортеж с количеством строк и столбцов
print(melb_data.shape)


# Для того чтобы получить более детальную информацию о столбцах таблицы, можно использовать метод DataFrame info():
print(melb_data.info())
 
 
# методом astype(), преобразовываем тип данных столбца
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')
 

# Чтобы быстро посмотреть на основные статистические свойства её столбцов можно воспользоваться методом DataFrame describe()
print(melb_data.describe().loc[:, ['Distance', 'BuildingArea' , 'Price']])


# include можно указать тип данных, для которого нужно вывести описательную информацию.
# percentiles Процентили, включаемые в вывод. Все значения должны находиться в диапазоне от 0 до 1. 
# Значение по умолчанию - [0,25, 0,5, 0,75], что возвращает 25, 50 и 75 процентили.
# include - выдает список в соответствии с типом данных
# exclude - исключает определенный тип данных 
# datetime_is_numeric - Считать ли типы datetime числовыми. 
# Это влияет на статистику, рассчитываемую для столбца. 
# Для ввода DataFrame это также определяет, включены ли столбцы datetime по умолчанию.
print(melb_data.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False))

# найти частоту для каждого уникального значения, используется метод value_counts().Данный метод возвращает объект Series, 
# в котором в качестве индексов выступают уникальные категории столбца, 
# а значениями — соответствующая им частота.
print(melb_data['Regionname'].value_counts())

# Чтобы сделать вывод более интерпретируемым и понятным, можно воспользоваться параметром normalize. 
# При установке значения этого параметра на True результат будет представляться в виде доли (относительной частоты):
print(melb_data['Regionname'].value_counts(normalize=True))


# Сколько процентов от общего количества домов составляют таунхаусы (тип объекта — t)?
# Если normalize=True, то возвращаемый объект будет содержать относительные частоты уникальных значений.
print(melb_data['Type'].value_counts(normalize=True))


# .mean()	Среднее значение
# Вычислим среднюю цену на объекты недвижимости:
print(melb_data['Price'].mean())


# .max()	Максимальное значение
# Найдём максимальное количество парковочных мест:
print(melb_data['Car'].max())


# А теперь представим, что риэлторская ставка для всех компаний за продажу недвижимости составляет 12%. 
# Найдём общую прибыльность риэлторского бизнеса в Мельбурне. Результат округлим до сотых:
rate = 0.12
income = melb_data['Price'].sum() * rate
print('Total income of real estate agencies:', round(income, 2))


# Найдём, насколько медианная площадь территории отличается от её среднего значения. 
# Вычислим модуль разницы между медианой и средним и разделим результат на среднее, чтобы получить отклонение в долях: 
landsize_median = melb_data['Landsize'].median() 
landsize_mean =  melb_data['Landsize'].mean()
print('насколько медианная площадь территории отличается от её среднего значения', abs(landsize_median - landsize_mean)/landsize_mean)

# Чему равно отклонение (в процентах) медианного значения площади здания от его среднего значения?
building_median = melb_data['BuildingArea'].median() 
building_mean =  melb_data['BuildingArea'].mean()
deviance = abs(building_median - building_mean)/building_mean
print('отклонение (в процентах) медианного значения площади здания от его среднего значения', round(deviance * 100, 2))


# В результате получаем долю отклонения медианы от среднего значения. 
# Умножив результат на 100, получим его в процентах. 
# Отклонение медианы от среднего значения на 21% является довольно большим, и это повод задуматься над тем, чтобы исследовать признак на наличие аномалий. 

# Какова средняя цена объектов недвижимости в таблице melb_data с ценой менее одного миллиона, 
# в которых либо количество комнат больше пяти, 
# либо здание моложе 2015 года?
print(round(melb_data[(melb_data['Price']<1e6) & ((melb_data['Rooms']>5) | (melb_data['YearBuilt'] > 2015))]['Price'].mean()))


# найдём медианную площадь здания у объектов, чья цена выше средней
# чтобы оградить наш код от нагромождений, предварительно создадим переменную со средней ценой:
mean_price = melb_data['Price'].mean()
print(melb_data[melb_data['Price'] > mean_price]['BuildingArea'].median())


# .count()	Количество непустых значений
# .min()	Минимальное значение
# .deviance()	Дисперсия
# .sum()	Сумма
# .quantile(x)	Квантиль уровня x
# .nunique()	Число уникальных значений
# axis  — определяет, подсчитывать параметр по строкам или по столбцам;
# numeric_only — определяет, вычислять параметры только по числовым столбцам/строкам или нет (True/False).


# МОДАЛЬНОЕ ЗНАЧЕНИЕ
# Модальных значений может быть несколько, то есть несколько значений могут встречаться одинаковое количество раз. 
# Поэтому метод mode(), в отличие от агрегирующих методов, возвращает не одно число, а серию.


# Вычислим, какое число комнат чаще всего представлено на рынке недвижимости:
print(melb_data['Rooms'].mode())


# Метод mode() может быть использован не только с числовыми столбцами, но и со столбцами типа object.
# найти наиболее распространённое название района:
print(melb_data['Regionname'].mode())


# В каком районе Мельбурна чаще всего продаются виллы и коттеджи (тип здания — h) с ценой меньше трёх миллионов?
print(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)]['Regionname'].mode())


# Сколько спален чаще всего встречается в домах в Мельбурне?
print('Сколько спален чаще всего встречается в домах в Мельбурне?', melb_data['Bedroom'].mode())


# Задан ряд чисел [1, 2, 4, 2, 3, 2, 1, 5, 6]. Чему равна мода в данном ряду?
x = [1, 2, 4, 2, 3, 2, 1, 5, 6]
result = pd.Series(x).mode()
print('Чему равна мода в данном ряду?', result)

# Но результатом операции тоже будет pandas.Series
# Поэтому чтобы только значение получить можно указать нулевой индекс
result = pd.Series(x).mode()[0]
print('Чему равна мода в данном ряду?', result)


# .std()	Стандартное отклонение
# Чему равно стандартное отклонение (разброс) расстояния от центра города до объекта недвижимости?
print('стандартное отклонение (разброс) расстояния от центра города до объекта недвижимости', round(melb_data['Distance'].std()))


# Фильтрация данных в DataFrame
mask = melb_data['Price'] > 2000000
print(melb_data[mask].head())

# не обязательно заносить маску в отдельную переменную — можно сразу вставлять условие в операцию индексации DataFrame, например:
print(melb_data[melb_data['Price'] > 2000000])


# Найдём количество зданий с тремя комнатами
print(melb_data[melb_data['Rooms'] == 3].shape[0])


# Усложним прошлый пример и найдём число трёхкомнатных домов с ценой менее 300 тысяч:
print(melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300000)].shape[0])


# У скольких объектов недвижимости из таблицы melb_data отсутствуют ванные комнаты?
print(melb_data[melb_data['Bathroom'] == 0].shape[0])# без shape выдаст список всех строк


# Сколько в таблице melb_data объектов недвижимости, которые были проданы риелтором Nelson 
# и стоимость которых составила больше 3 миллионов?
print(melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3000000)].shape[0])
# melb_data[(melb_data['SellerG'] == 'Nelson') & (melb_data['Price'] > 3e6)].shape[0]


# теперь нас будут интересовать дома с ценой менее 300 тысяч, 
# у которых либо число комнат равно 3 
# либо площадь домов более 100 квадратных метров:
print(melb_data[((melb_data['Rooms'] == 3) | (melb_data['BuildingArea'] > 100)) & (melb_data['Price'] < 300000)].shape[0])


# найдём максимальное количество комнат в таунхаусах
print(melb_data[melb_data['Type'] == 't']['Rooms'].max())


# Чему равно максимальное количество домов на продажу в районе (Propertycount)?
print('Propertycount', melb_data['Propertycount'].max())


# Какова минимальная стоимость участка без здания (площадь здания равна 0) в таблице melb_data?
print(melb_data[melb_data['BuildingArea'] == 0]['Price'].min())