import pandas as pd
import matplotlib.pyplot as plt

display = print


# Открытие и знакомство с данными

# читаем данные из csv, который находится в zip-файле на github
url = 'https://github.com/obulygin/SkillFactory/blob/main/ecommerce-data.zip?raw=true'
df = pd.read_csv(url, encoding='ISO-8859-1', compression='zip')


# смотрим первые 5 строк таблицы
#display(df.head())
# смотрим последние 5 строк таблицы
#display(df.tail())


# рассчитываем базовые статистики по каждому числовому признаку
df.describe() 


# Избавимся от отрицательных значений

# оставляем данные только с положительными ценами на товар и количеством
df = df[(df['UnitPrice'] > 0) & (df['Quantity'] > 0)]
df.describe()


# Избавимся от дубликатов в данных
# посмотрим, сколько у нас повторов
#print(df.duplicated().sum())

# сколько всего строк?
#print(df.shape)


# Поправим типы данных
#print(df.info())
df['CustomerID'] = df['CustomerID'].astype('Int64') # заменяем i  на I чтобы не было ошибок с пропусками
# Справка по ссылке
# Nullable datatypes: https://pandas.pydata.org/pandas-docs/stable/user_guide/integer_na.html


# переведем даты из строкового формата в datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


# Изучаем статистику по странам
# считаем сколько транзакций было по странам при помощи value_counts
#print(df['Country'].value_counts())


# считаем сколько уникальных клиентов в странах
countries = df.groupby('Country')['CustomerID'].nunique().sort_values(ascending=False)
#print(countries)


# Определяем топ-5 лояльных клиентов по количеству покупок
clients = df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False) 
#print(clients.head(5))


# Создадим временные признакми

# добавим месяц покупки в новый столбец при помощи dt.strftime('%Y - %m')
df['InvoiceMonth'] = df['InvoiceDate'].dt.strftime('%Y-%m') 
#print(df['InvoiceMonth'])

# уникальные покупатели по месяцам
df.groupby('InvoiceMonth')['CustomerID'].nunique()

df.groupby('InvoiceMonth')['CustomerID'].nunique().plot() # построим линейчатый график динамики

# зафиксируем дни недели
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek + 1

# посчитаем количество заказов по дням недели
df.groupby('DayOfWeek')['InvoiceNo'].nunique()


# Изучим динамику количества покупок по часам
df['InvoiceHour'] = df['InvoiceDate'].dt.hour
df.groupby('InvoiceHour')['InvoiceNo'].nunique() 


# Посчитаем выручку
# создадим новый столбец
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# выручка по месяцам
df.groupby('InvoiceMonth')['Revenue'].sum().plot(kind='bar')


# Найдите 3 страны, которые принесли максимальную выручку после UK
# так можно подавить scientific notation
pd.set_option('display.float_format', None)
df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(4)


# Сегменты товаров по стоимости
# напишем функцию для сегментации товаров
def price_segment(row):
    if row < 5:
        return 'cheap' 
    if 5 <= row < 25:
        return 'lower-middle'
    if 25 <= row < 100:
        return 'upper-middle'
    if row >= 100:
        return 'expensive'
 

df['PriceSegment'] = df['UnitPrice'].apply(price_segment)
df['PriceSegment'].value_counts()


# Определить, какая из категорий товаров принесла больше всего выручки
df.groupby('PriceSegment')['Revenue'].sum().sort_values(ascending=False) 


# Как меняется средний чек со временем?
df.groupby('InvoiceMonth')['Revenue'].sum().divide(df.groupby('InvoiceMonth')['InvoiceNo'].nunique())


# Построим сводные таблицы
# сводная таблица по выручки в определенной стране в разрезе пользователей и месяцев
country = 'France'
table = pd.pivot_table(
    df[df['Country']==country], 
    index='CustomerID', 
    columns='InvoiceMonth', 
    aggfunc=sum, 
    values='Revenue', 
    fill_value=0)

#print(table.round(3))

# подсветить максимальные значения по каждому месяцу
# table.style.highlight_max()
# table.style.background_gradient(cmap='PuBu')


# Построить сводную таблицу c кол-вом заказов по странам и месяцам
table_2 = pd.pivot_table(
    df, 
    index='Country', 
    columns='InvoiceMonth', 
    aggfunc='nunique', 
    values='InvoiceNo', 
    fill_value=0) 


# изучим сводную статистику по покупателям из произвольной страны (суммарная и средняя выручка)
products = df[df['Country']==country].groupby(['CustomerID', 'InvoiceNo'], as_index=False)['Revenue'].sum()
 
products = products.groupby('CustomerID').agg({'InvoiceNo': ['count'], 'Revenue': ['sum','mean']})
#print(products)

# объединяем статистику по месяцам и статистику по выручки и количеству заказов в разрезе пользователей
products.columns = [tup[1] if tup[1] else tup[0] for tup in products.columns]
table_plus = table.merge(products, on='CustomerID')

#print(table_plus)

# table_plus.style.highlight_max()
# table_plus.style.background_gradient(cmap='PuBu')


# Когортный анализ
"""
Идея когортного анализа состоит в том, чтобы резделить пользоватей на группы по определенным признакам, и отслеживать поведение этих групп во времени. Обычно группы пользователей (когорты) выделяют на основе недели (месяца), когда пользователи совершили первую покупку.
Выделив такие группы пользователей (когорты), вы следите за ними в течение времени и измеряете ключевые метрики для каждой отдельной когорты.
"""
# определяем месяц первой покупки для каждого покупателя 
cohorts = df.groupby('CustomerID', as_index=False)['InvoiceMonth'].min()
cohorts.rename(columns = {'InvoiceMonth':'Cohort'}, inplace=True)

# добавим когорты к основным данным
# исключаем пропуски по пользователям для корректного объединения
df_merged = pd.merge(df.dropna(), cohorts, how='left', on='CustomerID')

# считаем доходы по когортам
df_merged.groupby('Cohort')['Revenue'].sum()


# Анализ retention
# Customer retention (удержание клиентов) 
# — это способность компании удерживать своих потребителей в течение определенного периода времени.

import numpy as np

# пишем функцию которая добавляет столбец с временем жизни каждой когорты
def cohort_period(df):
  df['CohortLT'] = np.arange(len(df))
  return df

# считаем сколько уникальных клиентов у нас в каждой когорте
cohorts = df_merged.groupby(['Cohort', 'InvoiceMonth'])[['CustomerID']].nunique()
cohorts = cohorts.groupby(level=0).apply(cohort_period)
cohorts.rename({'CustomerID': 'TotalUsers'}, inplace=True)

# переведем когорты в индекс, а дату чека в столбец
cohorts.reset_index(inplace=True)
cohorts.set_index(['Cohort', 'CohortLT'], inplace=True) 

# считаем retention пользователей в каждой когорте
# определим количество покупок в первый месяц когорты (100%)
cohort_group_size = cohorts['CustomerID'].groupby(level=0).first()

# узнаем какой процент покупок этой когортой совершался в последующие месяца
user_retention = cohorts['CustomerID'].unstack(0).divide(cohort_group_size, axis=1)