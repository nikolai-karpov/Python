import pandas as pd

melb_df = pd.read_csv('data/melb_data_fe.csv')


# Преобразуйте столбец Date в формат datetime 
melb_df['Date'] = pd.to_datetime(melb_df['Date'])


# и выделите квартал (quarter) продажи объектов недвижимости. 
# обратившись по атрибуту dt.quarter в столбце Date, мы можем «достать» квартал продажи
quarter_sold = melb_df['Date'].dt.quarter
print('quarter sold:', quarter_sold.value_counts(normalize=True))


# Найдите второй по популярности квартал продажи. 
melb_df['QuarterSale'] = melb_df['Date'].dt.quarter


# Вывести на экран число объектов, проданных во втором по популярности квартале.
print(melb_df['QuarterSale'].value_counts())


# Преобразуйте все столбцы, в которых меньше 150 уникальных значений, в тип данных category
cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']           # исключив из преобразования столбцы Date, Rooms, Bedroom, Bathroom, Car.
max_unique_count = 150                                                      # задаём максимальное число уникальных категорий
for col in melb_df.columns:                                                 # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category')                      # преобразуем тип столбца


# МЕТОД SORT_VALUES()
# by — имя или список имён столбцов, по значениям которых производится сортировка.

# Отсортируем таблицу по возрастанию цены объектов недвижимости (Price):
print(melb_df.sort_values(by='Price').head(10))

# Отсортируем таблицу по убыванию (от самой последней до самой первой) даты продажи объекта (Date)
print(melb_df.sort_values(by='Date', ascending=False))  # ascending — сортировка по возрастанию (от меньшего к большему). 
                                                        # По умолчанию параметр выставлен на True, 
                                                        # для сортировки по убыванию (от большего к меньшему) необходимо выставить его на False.
                                                        
                                                        
# СОРТИРОВКА ПО ЗНАЧЕНИЯМ НЕСКОЛЬКИХ СТОЛБЦОВ

# отсортируем таблицу сначала по возрастанию расстояния от центра города (Distance), 
# а затем — по возрастанию цены объекта (Price). 
print(melb_df.sort_values(by=['Distance', 'Price']).loc[::10, ['Distance', 'Price']])   # важно обращать внимание на порядок следования столбцов.
# Мы получили таблицу, отсортированную по возрастанию расстояния до центра города. 
# Если встречаются объекты недвижимости, у которых расстояние оказывается одинаковым, то внутри такой группы производится сортировка по цене объекта.


# КОМБИНИРОВАНИЕ СОРТИРОВКИ С ФИЛЬТРАЦИЕЙ

# восстановить хронологию продаж таунхаусов, у которых площадь участка существенно больше площади здания, 
# чтобы понять, как часто компания справляется с таким сложным видом объектов. 
# Объекты, проданные в один и тот же день, мы бы хотели сортировать по значению коэффициента соотношения площадей. 

mask2 = melb_df['Type'] == 'townhouse'  # Найдём информацию о таунхаусах (Type)
mask3 = melb_df['SellerG'] == 'McGrath' # проданных компанией (SellerG) McGrath
mask1 = melb_df['AreaRatio'] < -0.8     # у которых коэффициент соотношения площадей здания и участка (AreaRatio) меньше -0.8.

print(melb_df[mask1 & mask2 & mask3].sort_values( 
    by=['Date', 'AreaRatio'],   # отсортируем по дате продажи (Date) в порядке возрастания, а после проведём сортировку по убыванию коэффициента соотношения площадей.
    ascending=[True, False],    
    ignore_index=True           # обновим старые индексы на новые, установив параметр ignore_index на True
).loc[:, ['Date', 'AreaRatio']])


# Произведите сортировку столбца AreaRatio по убыванию. 
melb_df_arearatio = melb_df.sort_values( 
    by=['AreaRatio'],
    ascending=[False],    # Для сортировки по убыванию (от большего к меньшему) необходимо False.
    ignore_index=True     # обновим старые индексы на новые
)

# Какое значение площади здания находится в строке 1558? 
print(round(melb_df_arearatio.loc[1558]['BuildingArea']))


# Найдите таунхаусы (Type) с количеством жилых комнат (Rooms) больше 2. 
mask4 = melb_df['Rooms'] > 2
melb_df_sorted_rooms = melb_df[mask2 & mask4].sort_values( 
    by=['Rooms', 'MeanRoomsSquare'],   # 
    ascending=[True, False],                # Отсортируйте полученную таблицу сначала по возрастанию числа комнат, а затем по убыванию средней площади комнат (MeanRoomsSquare). 
    ignore_index=True                       # Индексы таблицы заменим на новые.
)
 
# Какая цена будет у объекта в строке 18? Ответ запишите в виде целого числа.
print(round(melb_df_sorted_rooms.loc[18]['Price']))