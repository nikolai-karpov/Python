import pandas as pd

melb_data = pd.read_csv('data/melb_data_ps.csv', sep=',')


# чтобы не переопределять переменную melb_data и тем самым не повредить первоначальный DataFrame, 
# создадим копию melb_df с помощью метода copy():
melb_df = melb_data.copy()

# вычислив количество уникальных адресов с помощью метода nunique():
print('Кол-во уникальных адресов: ', melb_df['Address'].nunique())



def get_street_type(address):
    exclude_list = ['N', 'S', 'W', 'E', 'Cl'] # Создаём список географических пометок
    address_list = address.split(' ')
    street_type = address_list[-1]          # Обрезаем список, оставляя в нём только последний элемент,
                                            # потенциальный подтип улицы, и заносим в переменную street_type.
    if street_type in exclude_list:         # Делаем проверку на то, что полученный подтип является географической пометкой.
        street_type = address_list[-2]      # Если переменная street_type является географической пометкой,
                                            # переопределяем её на второй элемент с конца списка address_list.
    if street_type == 'Avenue':
        return 'Av'
    if street_type == 'Parade':
        return 'Pde'
    if street_type == 'Boulevard':
        return 'Bvd'
    if street_type == 'Highway':
        return 'Hwy'
    if street_type == 'Center':
        return 'Ctr'
    if street_type == 'Cr':
        return 'Ctr'
    if street_type == 'Drive':
        return 'Dr'
    if street_type == 'Lane':
        return 'Ln'
    if street_type == 'La':
        return 'Ln'
    if street_type == 'Parkway':
        return 'Prwy'
    if street_type == 'Place':
        return 'Pl'
    if street_type == 'Quay':
        return 'Qy'
    if street_type == 'Square':
        return 'Sq'
    if street_type == 'Street':
        return 'St'
    if street_type == 'Terrace':
        return 'Tce'
    if street_type == 'Court':
        return 'Ct'
    return street_type
    
'''
melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
melb_df['StreetType'] = melb_df['StreetType'].apply(lambda x: 'Av' if x == 'Avenue')
melb_df['StreetType'] = street_types.apply(lambda x: 'Av' if x == 'Avenue' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Pde' if x == 'Parade' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Bvd' if x == 'Boulevard' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Hwy' if x == 'Highway' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Ctr' if x == 'Center' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Dr' if x == 'Drive' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Ln' if x == 'Lane' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Prwy' if x == 'Parkway' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Pl' if x == 'Place' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Qy' if x == 'Quay' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'Sq' if x == 'Square' else x)
melb_df['StreetType'] = street_types.apply(lambda x: 'St' if x == 'Street' else x)

print('(После чистки) Частота каждого подтипа улицы: ', street_types.value_counts())
'''



# Теперь применим эту функцию к столбцу c адресом. 
# Для этого передадим функцию get_street_type в аргумент метода столбца apply(). 
street_types = melb_df['Address'].apply(get_street_type)    # В результате получим объект Series, который положим в переменную street_types

# Обратите внимание, что функция пишется для одного элемента столбца, а метод apply() применяется к каждому его элементу. 
# Используемая функция обязательно должна иметь возвращаемое значение.
print('Уникальных типов улиц: ', street_types.nunique())


# частота каждого подтипа улицы с помощью метода value_counts:
print('Частота каждого подтипа улицы: ', street_types.value_counts())


# применим очень распространённый метод уменьшения количества уникальных категорий — выделим n подтипов, 
# которые встречаются чаще всего, а остальные обозначим как 'other' (другие).
# Для этого к результату метода value_counts применим метод nlargest(), 
# который возвращает n наибольших значений из Series. 
# Извлечём их названия с помощью атрибута index, а результат занесём в переменную popular_stypes:
popular_stypes = street_types.value_counts().nlargest(10).index # Зададим n=10, т. е. мы хотим отобрать десять наиболее популярных подтипов. 
print('Популярные типы улиц: ', popular_stypes)


# Теперь, когда у нас есть список наиболее популярных подтипов улиц, введём lambda-функцию, 
# которая будет проверять, есть ли строка x в этом перечне, 
# и, если это так, lambda-функция будет возвращать x, в противном случае она будет возвращать строку 'other'. 
# Наконец, применим такую функцию к Series street_types, полученной ранее, а результат определим в новый столбец таблицы StreetType:


melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
print('Уникальных типов улиц после сортировки лямбда: ', melb_df['StreetType'].nunique())


# Теперь, у нас нет потребности хранить признак Address, 
# так как, если конкретное местоположение объекта всё же и влияет на его стоимость, то оно определяется столбцами Longitude и Lattitude. 
# Удалим его из нашей таблицы:
melb_df = melb_df.drop('Address', axis=1)

# Таким образом, с помощью написания собственных функций и их комбинирования с методом apply() 
# из библиотеки Pandas мы смогли извлечь информацию из признака с адресом и заменить на признак подтипа улицы. 


# Примечание. Мы допустили небольшую ошибку!
# в списке подтипов улиц street_types подтипы  Av и Avenue, Bvd и Boulevard, Pde и Parade. - Это грязные данные
# написать функцию-преобразование (lambda-функцию-преобразование), 
# которая возвращала бы вместо значений Avenue, Boulevard и Parade их топографические сокращения, 
# Данное преобразование необходимо применить к данным о подтипах улиц до сокращения количества уникальных категорий.