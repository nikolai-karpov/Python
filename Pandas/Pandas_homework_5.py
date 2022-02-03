import pandas as pd

melb_data = pd.read_csv('data/melb_data_ps.csv', sep=',')


# чтобы не переопределять переменную melb_data и тем самым не повредить первоначальный DataFrame, 
# создадим копию melb_df с помощью метода copy():
melb_df = melb_data.copy()


# Удалим столбцы index и Coordinates из таблицы с помощью метода drop()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)


# Преобразуем столбец Date в формат datetime:
melb_df['Date'] = pd.to_datetime(melb_df['Date'])


# Создадим признак WeekdaySale
# Найдите, сколько объектов недвижимости было продано в выходные (суббота и воскресенье)
melb_df['WeekdaySale'] = melb_df['Date'].dt.dayofweek                                           # номер дня недели, где 0 — понедельник, 6 — воскресенье
print(melb_df['WeekdaySale'])                                                                   # день недели в который продан объект
weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0] # сколько продаж в пятницу и субботу
print('В выходные продано', weekend_count, 'объектов')


# Напишите функцию, которая принимает на вход элемент столбца WeekdaySale 
# Результат округлите до сотых.

    
def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1                        # возвращает 1, если день является выходным
    else: 
        return 0                        # 0 — в противном случае
    
    
melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)  # Создаём столбец Weekend в таблице melb_df с помощью функции get_weekend.

print('Средняя цена объекта недвижимости, проданного в выходные дни', round(melb_df[melb_df['Weekend']==1]['Price'].mean(), 2))#  Средняя цена объекта недвижимости, проданного в выходные дни. 


# Преобразуйте столбец SellerG с наименованиями риелторских компаний в таблице melb_df следующим образом: 
# оставьте в столбце только 49 самых популярных компаний nlargest(49), а остальные обозначьте как 'other'.
popular_sellers = melb_df['SellerG'].value_counts().nlargest(49).index      # Извлечём их названия с помощью атрибута index

# введём lambda-функцию, которая будет проверять, есть ли строка x в этом перечне popular_sellers
# и, если это так, lambda-функция будет возвращать x, в противном случае она будет возвращать строку 'other'. 
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_sellers else 'other')
print('[SellerG].nunique: ', melb_df['SellerG'].nunique())


# Найдите, во сколько раз минимальная цена объектов недвижимости, проданных компанией 'Nelson'
a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min() 

# больше минимальной цены объектов, проданных компаниями, обозначенными как 'other'. 
b = melb_df[melb_df['SellerG'] == 'other']['Price'].min() 

# Ответ округлите до десятых.
print('минимальная цена объектов, проданных Nelson в', round(a/b, 1), 'раза больше минимальной цены , проданных как other')