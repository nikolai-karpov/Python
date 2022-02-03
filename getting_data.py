import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sber_data = pd.read_csv('homework/data/sber_data.csv')


# Сколько районов Москвы и Московской области представлено в данных?
sber_data.groupby('sub_area').nunique()


# Чему равна максимальная цена квартир (price_doc)? 
# Присмотритесь к нему — не кажется ли оно вам странным? Мы к нему ещё вернемся :)
price_doc = sber_data['price_doc']
price_doc.max()


# Проверим, влияет ли уровень экологической обстановки в районе на цену квартиры. 
# Постройте коробчатую диаграмму цен на квартиры (price_doc) в зависимости от уровня экологической обстановки в районе (ecology). 
# Какой уровень ценится на рынке меньше всего?
price_ecology = sber_data.copy()[['price_doc', 'ecology']]

fig = plt.figure('Влияние уровеня экологичности района на цену квартиры')
fig.suptitle('Влияние уровеня экологичности района на цену квартиры', fontsize=14)
ax = fig.add_axes([0,1.1,1,1])

sns.boxplot(
    ax=ax, 
    data=price_ecology, 
    y='ecology', 
    x='price_doc', 
    orient='h'
);


# Постройте диаграмму рассеяния, которая покажет, как цена на квартиру (price_doc) связана с расстоянием до центра Москвы
