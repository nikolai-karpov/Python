import pandas as pd
import numpy as np

amazon_df = pd.read_csv('https://raw.githubusercontent.com/AndreyRysistov/VebinarDST/main/amazon_com_data.csv')

print('Количество строк: {}'.format(amazon_df.shape[0]))
print('Количество столбцов: {}'.format(amazon_df.shape[1]))
print('Список столбцов: ', list(amazon_df.columns))

# Столбцы:
"""
product_name - название товара
mrp - цена без скидки
price - цена на сайте
pdp_url - ссылка на товар
brand_name - название бренда
product_category - категория товара
retailer - ретейлер
description - описание
rating - рейтинг товара
review count - количество отзывов
style attributes - состав товара
total sizes - все размеры
available size - доступные размеры
color - цвет
"""

amazon_df.describe()#описание по числовым столбцам

# Для того, чтобы посмотреть информацию для других типов данных используется параметр include:
amazon_df.describe(include=['object'])
# Нужно проверять чтоб цифровые толбцы не были object

# Удалим лишнюю информацию
amazon_df.drop(['pdp_url', 'description', 'retailer', 'total_sizes', 'available_size', 'style_attributes'], axis=1, inplace=True)# inplace=True - изначальная таблица перезапишется


# Немного предобработаем данные
# str.replace('$', '') убираем знак доллар
amazon_df['mrp'] = amazon_df['mrp'].str.replace('$', '').astype('float64') * 72.85
amazon_df['price'] = amazon_df['price'].str.replace('$', '').astype('float64') * 72.85
amazon_df.head(1)

# вопросов для анализа:
"""
если среднее не отличается от медианы тогда вбросов меньше
если разница между 0.25% и 0.75% близка к стандартному отклонению значит вбросов мало
"""
# Каково распределение цен на товары?
# Как цена и рейтинг товаров зависят от бренда?
# Какую цветовую гамму предпочитают различные бренды?
# На какие категориии товаров идут наибольшие скидки?


# Найдем статистические характеристики для цен на товары и построим гистограмму:
print('Средняя цена товаров (руб): ', amazon_df['price'].mean())
print('Медианная цена товаров (руб): ', amazon_df['price'].median())
print('Минимальная цена товаров (руб): ', amazon_df['price'].min())
print('Максимальная цена товаров (руб): ', amazon_df['price'].max())
print('Стандартное отклонение цены на товары (руб): ', amazon_df['price'].std())
print(amazon_df['price'].hist())


# Найдем средний рейтинг товаров бренда Calvin Klein
amazon_df[amazon_df['brand_name'] == 'Calvin-Klein']['rating'].mean()


# найдем насколько средняя цена бюстгалтеров в Victorias-Secret отличается от той же категории товаров в Wacoal
vs_mean_price = amazon_df[(amazon_df['brand_name'] == 'Victorias-Secret') & (amazon_df['product_category'] == 'Bras')]['price'].mean()
wc_mean_price = amazon_df[(amazon_df['brand_name'] == 'Wacoal') & (amazon_df['product_category'] == 'Bras')]['price'].mean()
vs_mean_price - wc_mean_price


# какова средняя скидка товаров на Amazon?
sale_data = amazon_df[amazon_df['mrp'] > amazon_df['price']]
mean_sale = (sale_data['mrp'] - sale_data['price']).mean()
mean_sale


# Какая взаимосвязь между количеством отзывов и рейтингом товара? 
# сильная взаимосвязь корреляция близка к единице
amazon_df['review_count'].corr(amazon_df['rating'])


# список всех уникальных брендов:
amazon_df['brand_name'].unique()


# Определим наиболее распространенное значение цвета для нескольких брендов. Для этого найдем модальное значение с помощью метода mode:
amazon_df[(amazon_df['brand_name'] == 'Victorias-Secret')]['color'].mode()[0]


print('Популярный цвета брендов:')
print('Victorias-Secret: ', amazon_df[(amazon_df['brand_name'] == 'Victorias-Secret')]['color'].mode()[0])
print('Calvin-Klein: ', amazon_df[(amazon_df['brand_name'] == 'Calvin-Klein')]['color'].mode()[0])
print('Wacoal: ', amazon_df[(amazon_df['brand_name'] == 'Wacoal')]['color'].mode()[0])
print('Hanky-Panky: ', amazon_df[(amazon_df['brand_name'] == 'Hanky-Panky')]['color'].mode()[0])


# список всех категорий товаров компании Calvin-Klein и число товаров для них
ck_df = amazon_df[(amazon_df['brand_name'] == 'Calvin-Klein')]
ck_df['product_category'].value_counts(normalize=True)


