import pandas as pd


# СПОСОБ 1 создания DataFrame — из словаря
# ключ - имена столбцов будущей таблицы, 
# значения — списки, в которых хранится содержимое этих столбцов:

countries_df = pd.DataFrame({
    'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
    'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
})
# Обратите внимание, что, так как мы не задали метки (индексы) DataFrame, они были сгенерированы автоматически. 
# Исправим это, задав индексы вручную:

countries_df.index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']

# Считаем среднее по строкам (axis = 0) в каждом столбце:
print('среднее по строкам', countries_df.mean(axis=0))
# В данном случае среднее было рассчитано по строкам для столбцов population и square.

# Можно обратиться к DataFrame по имени столбца через точку
# Однако использование такого способа возможно только тогда, когда имя столбца указано без пробелов:
print('countries_df.population', countries_df.population)


# СПОСОБ 2 создать из вложенного списка, 
# внутренние списки которого будут являться строками новой таблицы
# В данном варианте создания DataFrame мы задаём имена столбцов в списке с помощью параметра columns, 
# а также инициализируем параметр index для задания меток стран.

countries_df_2 = pd.DataFrame(
    data = [
        ['Англия', 56.29, 133396],
        ['Канада', 38.05, 9984670],
        ['США', 322.28, 9826630],
        ['Россия', 146.24, 17125191],
        ['Украина', 45.5, 603628],
        ['Беларусь', 9.5, 207600],
        ['Казахстан', 17.04, 2724902]
    ],
    columns= ['country', 'population', 'square'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ']
)

# Здесь среднее было рассчитано по числовым столбцам для каждой строки в таблице.
print('среднее по столбцам', countries_df_2.mean(axis=1))

# Другой вариант — обратиться к DataFrame по индексу и указать имя столбца:
print('countries_df[population]', countries_df['population'])


# Получим площадь Великобритании:
print('площадь Великобритании', countries_df.loc['UK', 'square'])


# Получим население и площадь, соответствующие России:
print('население и площадь России', countries_df.loc['RU', ['population', 'square']])


# Сделаем вырезку из таблицы и получим информацию о населении и площади, соответствующую 
# Украине, Беларуси и Казахстану:
print(countries_df.loc[['UA', 'BY', 'KZ'],['population', 'square']])
# или
print(countries_df.iloc[4:8, 1:3])


# При создании DataFrame из вложенных списков его внутренние списки являются строками таблицы.
pd.DataFrame([[0,1], [1, 0]], columns=['А', 'B'])
#   A B
# 0 0 1
# 1 1 0

# При создании DataFrame из словаря значения словаря — это значения в столбцах будущей таблицы.
pd.DataFrame({'А': [0, 1], 'B': [1, 0]})
#   A B
# 0 0 1
# 1 1 0

countries = pd.Series(
    data = ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
    index = ['UK', 'CA', 'US', 'RU', 'UA', 'BY', 'KZ'],
    name = 'countries'
)
# Если оставить параметр index пустым, 
# то метки будут присвоены автоматически в виде порядковых номеров элементов

print(countries)


# Способ 2 — из словаря, в котором ключами являются будущие метки, 
# а значениями — будущие значения Series

countries_2 = pd.Series({
    'UK': 'Англия',
    'CA': 'Канада',
    'US': 'США',
    'RU': 'Россия',
    'UA': 'Украина',
    'BY': 'Беларусь',
    'KZ': 'Казахстан'},
    name = 'countries'
)
print(countries_2)


# .loc вызывается с квадратными скобками, в которые передаются метки
# Для того чтобы достать информацию по нескольким индексам, 
# необходимо обернуть интересующие индексы в список:
print(countries.loc[['US', 'RU', 'UK']])

# в случае обращения по одному индексу возвращается строка. 
# Если же обратиться по нескольким элементам, возвращается объект Series.


# .iloc также вызывается с квадратными скобками и принимает на вход порядковые номера элементов Series
# Получим срез из исходной Series с первого по третий элемент:
print(countries.iloc[1:4])


# берутся элементы с порядковыми номерами от 1 до 4, не включая последний

