import pandas as pd
melb_df = pd.read_csv('data/melb_data_fe.csv')
melb_df['Date'] = pd.to_datetime(melb_df['Date'])


# Группировка данных в DataFrame

# МЕТОД GROUPBY()
# by — имя или список имён столбцов, по которым производится группировка.
# axis — ось, по которой производится группировка (0 — строки, 1 — столбцы). По умолчанию группировка производится по строкам.
# as_index — добавляется ли дополнительный индекс к таблице. По умолчанию установлен на True.

print(melb_df.groupby(by='Type').mean())

# Если мы хотим видеть тип объекта в качестве отдельного столбца таблицы, мы можем выставить параметр as_index на False:
print(melb_df.groupby(by='Type', as_index=False).mean())


# сравним средние цены на объекты в зависимости от их типа:
print(melb_df.groupby('Type')['Price'].mean())


# какие регионы (Regionname) наиболее удалены от центра Мельбурна
print(melb_df.groupby('Regionname')['Distance'].min().sort_values(ascending=False))


# ГРУППИРОВКА ДАННЫХ ПО ОДНОМУ КРИТЕРИЮ С НЕСКОЛЬКИМИ АГРЕГАЦИЯМИ
# Чтобы рассчитать несколько агрегирующих методов, можно воспользоваться методом agg(), который принимает список строк с названиями агрегаций.


# анализ продаж по месяцам
# найдём количество продаж count, а также среднее mean и максимальное значения max цен объектов недвижимости (Price)
# сгруппированных по номеру месяца продажи groupby('MonthSale')['Price']
# Результат отсортируем по количеству продаж count в порядке убывания:
print(melb_df.groupby('MonthSale')['Price'].agg(
    ['count', 'mean', 'max']                        # список с названиями интересующих нас агрегирующих функций
).sort_values(by='count', ascending=False))


# полная информация обо всех основных статистических характеристиках внутри каждой группы
print(melb_df.groupby('MonthSale')['Price'].agg('describe'))


# число уникальных риелторских компаний в зависимости от региона
# чтобы понять, в каких регионах конкуренция на рынке недвижимости меньше

print(melb_df.groupby('Regionname')['SellerG'].agg(
    		['nunique', set]    # Передадим дополнительно встроенную функцию set, чтобы получить множество из агентств недвижимости, которые работают в каждом из регионов:
))


# Сгруппируйте данные по признаку количества комнат 
# и найдите среднюю цену объектов недвижимости в каждой группе. 
print(melb_df.groupby('Rooms')['Price'].mean().sort_values(ascending=False))


# Какой регион имеет наименьшую протяжённость по географической широте (Lattitude)?
# Для ответа на этот вопрос рассчитайте стандартное отклонение широты для каждого региона.
print(melb_df.groupby('Regionname')['Lattitude'].std().sort_values())


# Какая риелторская компания (SellerG) имеет наименьшую общую выручку за период с 1 мая по 1 сентября (включительно) 2017 года?
# рассчитайте сумму продаж (Price) каждой компании в заданный период.
date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_df['Date']) & (melb_df['Date']<= date2)
print(melb_df[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True))


# МЕТОД GROUPBY КАК СПОСОБ ПОСТРОЕНИЯ СВОДНЫХ ТАБЛИЦ

# построить зависимость медианной цены и площади здания от числа комнат:
print(melb_df.groupby(['Rooms'])[['Price', 'BuildingArea']].median())

# будем учитывать не только число комнат, но и тип здания (Type)
# Чтобы финальный результат был представлен в виде таблицы, к результату агрегирования применим метод unstack():
print(melb_df.groupby(['Rooms', 'Type'])['Price'].mean().unstack())


# МЕТОД PIVOT_TABLE ДЛЯ ПОСТРОЕНИЯ СВОДНЫХ ТАБЛИЦ
# values — имя столбца, по которому необходимо получить сводные данные, применяя агрегирующую функцию;
# index — имя столбца, значения которого станут строками сводной таблицы;
# columns — имя столбца, значения которого станут столбцами сводной таблицы;
# aggfunc — имя или список имён агрегирующих функций (по умолчанию — подсчёт среднего, 'mean');
# fill_value — значение, которым необходимо заполнить пропуски (по умолчанию пропуски не заполняются).

# Давайте построим ту же самую таблицу, но уже с использованием метода pivot_table
print(melb_df.pivot_table(
    values='Price',
    index='Rooms',
    columns='Type',
    fill_value=0
).round())


# проанализируем продажи в каждом из регионов в зависимости от того, будний был день или выходной
print(melb_df.pivot_table(
    values='Price',
    index='Regionname',
    columns='Weekend',
    aggfunc='count',
))


# Найдём, как зависит средняя и медианная площадь участка (Landsize) от типа объекта (Type) и его региона (Regionname).
# Чтобы посмотреть несколько статистических параметров, нужно передать в аргумент aggfunc список из агрегирующих функций
print(melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    aggfunc=['median', 'mean'],
    fill_value=0
))


# МНОГОМЕРНЫЕ СВОДНЫЕ ТАБЛИЦЫ
# Давайте построим таблицу, в которой по индексам будут располагаться признаки метода продажи (Method) и типа объекта (Type), 
# по столбцам — наименование региона (Regionname), 
# а на пересечении строк и столбцов будет стоять медианная цена объекта (Price):
print(melb_df.pivot_table(
    values='Price',
    index=['Method','Type'],
    columns='Regionname',
    aggfunc='median',
    fill_value=0
))


# ДОСТУП К ДАННЫМ В СВОДНОЙ ТАБЛИЦЕ
pivot = melb_df.pivot_table(
    values='Landsize',
    index='Regionname',
    columns='Type',
    aggfunc=['median', 'mean'],
    fill_value=0
)

# Выведем её столбцы с помощью атрибута columns:
print(pivot.columns)

# Так, из таблицы pivot мы можем получить средние значения площадей участков для типа здания unit, просто последовательно обратившись по имени столбцов:
print(pivot['mean']['unit'])


# регионы, в которых средняя площадь здания для домов типа house меньше их медианной площади:
mask = pivot['mean']['house'] < pivot['median']['house']
filtered_pivot = pivot[mask]
print(filtered_pivot)

# Чтобы получить индексы отфильтрованной таблицы, можно воспользоваться атрибутом index и обернуть результат в список:
print(list(filtered_pivot.index))


# Составьте сводную таблицу, которая показывает зависимость медианной площади (BuildingArea) здания от типа объекта недвижимости (Type) и количества жилых комнат в доме (Rooms). 
# Для какой комбинации признаков площадь здания наибольшая?
pivot = melb_df.pivot_table(
    values='BuildingArea',
    index='Rooms',
    columns='Type',
    aggfunc=['median'],
    fill_value=0
)
print(pivot)


pivot = melb_df.pivot_table(
    values='BuildingArea',
    index='Type',
    columns='Rooms',
    aggfunc=['median'],
    fill_value=0
)
print(pivot)


# Зависимость средней цены объекта недвижимости (Price) от риелторского агентства (SellerG) и типа здания (Type).
# Во вновь созданной таблице найдите агентство, у которого средняя цена для зданий типа unit максимальна. 

pivot = melb_df.pivot_table(
    values='Price',
    index='SellerG',
    columns='Type',
    aggfunc='mean',
    fill_value=0
)
print(pivot)
max_unit_price = pivot['unit'].max()
print('max_unit_price: ', max_unit_price)
print(pivot[pivot['unit'] == max_unit_price].index[0])