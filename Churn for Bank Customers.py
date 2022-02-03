import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# import plotly
# import plotly.graph_objs as go
#from plotly.subplots import make_subplots
#import cufflinks


churn_data = pd.read_csv('data/content/churn.csv')
# churn_data = pd.read_csv('https://github.com/nikolai-karpov/sf_data_science/blob/436abde6f542c832c4d840b521627df255d63aaa/data/churn.csv?raw=true')


"""
Столбцы таблицы:
1. RowNumber    — номер строки таблицы (это лишняя информация, поэтому можете сразу от неё избавиться)
2. CustomerId   — идентификатор клиента
3. Surname      — фамилия клиента
4. CreditScore  — кредитный рейтинг клиента (чем он выше, тем больше клиент брал кредитов и возвращал их)
5. Geography    — страна клиента (банк международный)
6. Gender       — пол клиента
7. Age          — возраст клиента
8. Tenure       — сколько лет клиент пользуется услугами банка
9. Balance      — баланс на счетах клиента в банке
10. NumOfProducts — количество услуг банка, которые приобрёл клиент
11. HasCrCard       — есть ли у клиента кредитная карта (1 — да, 0 — нет)
12. IsActiveMember  — есть ли у клиента статус активного клиента банка (1 — да, 0 — нет)
13. EstimatedSalary — предполагаемая заработная плата клиента
14. Exited          — статус лояльности (1 — ушедший клиент, 0 — лояльный клиент)
"""

churn_data.drop(columns='RowNumber', inplace=True) # Избавляемся от ненужно строки

# Оптимизируем занимаемую память
churn_data['Age'] = churn_data['Age'].astype(np.int8)
churn_data['Tenure'] = churn_data['Tenure'].astype(np.int8)
churn_data['NumOfProducts'] = churn_data['NumOfProducts'].astype(np.int8)
churn_data['HasCrCard'] = churn_data['HasCrCard'].astype(np.int8)
churn_data['IsActiveMember'] = churn_data['IsActiveMember'].astype(np.int8)
churn_data['Exited'] = churn_data['Exited'].astype(np.int8)

# Выделяем категориальные признаки
churn_data['Gender'] = churn_data['Gender'].astype('category')
churn_data['Geography'] = churn_data['Geography'].astype('category')


# Задаем общий стиль
sns.set_style("whitegrid")
colors = sns.color_palette("pastel")
figsize = (6, 4)
figsize2 = (10, 4)
figsize3 = (14, 4)


# ЗАДАНИЯ

# 9.1. Каково соотношение ушедших Exited 1 и лояльных клиентов Exited 0? 
# Покажите это на графике и дайте комментарий по соотношению (Пирог).
percentage = churn_data.groupby('Exited')['Exited'].count().transform(lambda x: x / churn_data.shape[0] * 100)  # делим подсчитанных клиентов на общее кол-во
"""
labels={'0':'Лояльные', '1':'Ушедшие'}

fig = px.pie(
    percentage, 
    values=percentage, 
    labels=labels,
    names='Exited',         # Легенда
    title='соотношение ушедших Exited 1 и лояльных клиентов Exited 0'
)

#fig.show()
"""

# Альтернатива
fig = plt.figure('9.1', figsize=figsize)
ax = fig.add_axes([0,0,1,1])
labels=['Лояльные', 'Ушедшие']

ax.pie(
    percentage, 
    explode=[0, 0.1], 
    labels=labels, 
    autopct='%1.1f%%',
    textprops={'fontsize': 14},
    startangle=37,
    colors=colors
)

ax.set_title('Соотношение лояльных и ушедших клиентов', fontsize=18);


# Колличественное распределение клиентов 
exited_data = churn_data['Exited'].value_counts()

fig = plt.figure('9.1.1', figsize=figsize)
plt.bar(
    labels, 
    exited_data, 
    color=colors    #["#a1c9f4", "#ffb482"]
)

plt.title('Сравнение групп клиентов', fontsize=12)
plt.xlabel('Клиенты', fontsize=12)
plt.ylabel('Количество, чел.', fontsize=12)

#plt.show()


# 9.2. Постройте график, показывающий распределение баланса пользователей, у которых на счету больше 2 500 долларов. 
# Опишите распределение и сделайте выводы.
sorted_2500 = churn_data[churn_data['Balance'] > 2500]                          # Делаем выборку клиентов у которых на счету больше 2 500 долларов.
summary_table_9_2 = sorted_2500.copy()[['Balance', 'Exited']]
summary_table_9_2['Статус клиента'] = summary_table_9_2['Exited'].apply(lambda x: 'Лояльный' if x == 0 else 'Ушедший')# Добавляем признак Статус клиента
summary_table_9_2.rename(columns={'Exited': 'Count'}, inplace=True)             # Переименовываем столбец счетчик

fig = plt.figure('9.2', figsize=figsize)
ax = fig.add_axes([0,0,1,1])

sns.histplot(
    data=summary_table_9_2, 
    x="Balance",            # По горизонтале размеры сумм на банковских счетах клиентов
    hue="Статус клиента",   # Группирующая переменная, которая будет создавать точки разных цветов
    multiple="stack",       # “layer” - один слой закроет второй, 
                            # “dodge” - столбцы не будут накладываться друг на друга, 
                            # “fill” - показывает в процентном соотношении
    bins = 25
)

ax.get_xticks(minor=False)
ax.set_xticklabels([f"{round(x)}K" for x in ax.get_xticks()/1000]) # округление по оси X

ax.set_title('Распределение средств клиентов с балансом > 2500 $', fontsize=18)
ax.set_xlabel('Баланс, $, тыс.', fontsize=18)
ax.set_ylabel('Количество, чел.', fontsize=18);

#plt.show()


# 9.3. Посмотрите на распределение баланса клиента в разрезе признака оттока. 
# Столбчатый график и boxplot
# Как различаются суммы на накопительном счёте ушедших и лояльных клиентов? 
# Подумайте и напишите, с чем это может быть связано, что может не устраивать ушедших клиентов в банке.
fig = plt.figure('9.3', figsize=figsize3)
fig.subplots_adjust(top=0.8)
fig.suptitle('Распределение баланса клиента в разрезе признака оттока', fontsize=18)

axes = fig.subplots(1, 3)
ax = axes[0]
ax1 = axes[1]
ax2 = axes[2]

sns.boxplot(
    ax=ax, 
    data=churn_data, 
    y='Exited', 
    x='Balance', 
    orient='h',                   # Горизонтальная расположение
    palette=[colors[0], colors[1]]
)

ax.get_xticks(minor=False)
ax.set_xticklabels([f"{round(x)}K" for x in ax.get_xticks()/1000])
ax.set_yticklabels(['Лояльные', 'Ушедшие'], fontsize=12, rotation=90, va='center')

ax.set_title('Распределение по лояльности', fontsize=14)
ax.set_xlabel('Баланс, $, тыс.', fontsize=12)
ax.set_ylabel('')


summary_table_9_3 = churn_data.copy()[['Balance', 'IsActiveMember', 'Exited']]                                # Делаем выборку Статус клиента и его данные активности и размер счета
summary_table_9_3['Exited'] = summary_table_9_3['Exited'].apply(lambda x: 'Лояльный' if x == 0 else 'Ушедший')  # Добавляем признак Статус клиента
summary_table_9_3['IsActiveMember'] = summary_table_9_3['IsActiveMember'].apply(lambda x: 'Активный' if x == 1 else 'Пассивный')# Добавляем признак Статус клиента
summary_table_9_3.rename(columns={'Exited': 'Статус клиента'}, inplace=True)                           # Переименовываем для легенды столбец Статус клиента
summary_table_9_3.rename(columns={'IsActiveMember': 'Активность клиента'}, inplace=True)                # Переименовываем для легенды столбец Активность клиента

# Лояльные
loyal_clients = summary_table_9_3[summary_table_9_3['Статус клиента'] == 'Лояльный'].reset_index() 
sns.histplot(
    ax=ax1,
    data=loyal_clients,
    x="Balance",          # По горизонтале размеры сумм на банковских счетах клиентов
    hue="Активность клиента",   # Группирующая переменная, которая будет создавать точки разных цветов
    multiple="stack",     # “layer” - один слой закроет второй, 
                          # “dodge” - столбцы не будут накладываться друг на друга, 
                          # “fill” - показывает в процентном соотношении
    bins = 25
)

ax1.get_xticks(minor=False)
ax1.set_xticklabels([f"{round(x)}K" for x in ax1.get_xticks()/1000]) # округление по оси X

ax1.set_title('Лояльные в разрезе активности', fontsize=14)
ax1.set_xlabel('Баланс, $, тыс.', fontsize=12)
ax1.set_ylabel('Количество, чел.', fontsize=12)


# Ушедшие
unloyal_clients = summary_table_9_3[summary_table_9_3['Статус клиента'] == 'Ушедший'].reset_index()

sns.histplot(
    ax=ax2,
    data=unloyal_clients,
    x="Balance",          # По горизонтале размеры сумм на банковских счетах клиентов
    hue="Активность клиента",   # Группирующая переменная, которая будет создавать точки разных цветов
    multiple="stack",     # “layer” - один слой закроет второй, 
                          # “dodge” - столбцы не будут накладываться друг на друга, 
                          # “fill” - показывает в процентном соотношении
    bins = 25
)

ax2.get_xticks(minor=False)
ax2.set_xticklabels([f"{round(x)}K" for x in ax1.get_xticks()/1000]) # округление по оси X

ax2.set_title('Ушедшие в разрезе активности', fontsize=14)
ax2.set_xlabel('Баланс, $, тыс.', fontsize=12)
ax2.set_ylabel('Количество, чел.', fontsize=12);

plt.show()


# Дополнительная аналитика сверх задания
loyal_clients_balance = loyal_clients['Balance'].sum()
unloyal_clients_balance = unloyal_clients['Balance'].sum()
print('На счетах банка: ', loyal_clients_balance)
print('Выведено со счетов банка ушедшими: ', unloyal_clients_balance)

unloyal_clients_active = unloyal_clients[unloyal_clients['Активность клиента'] == 'Активный']
unloyal_clients_active_balance = unloyal_clients_active['Balance'].sum()
print('Активными клиентами выведено: ', unloyal_clients_active_balance)
print('Потенциально недополученный оборот', round(unloyal_clients_active_balance/loyal_clients_balance*100), '%')


#plt.show()


# 9.4. Посмотрите на распределение возраста в разрезе признака оттока. 
# В какой группе больше потенциальных выбросов? 
# На какую возрастную категорию клиентов стоит обратить внимание банку?
fig = plt.figure('9.4', figsize=figsize3)
fig.subplots_adjust(top=0.8)
fig.suptitle('Распределение возраста в разрезе признака оттока', fontsize=18)

axes = fig.subplots(1, 3)
ax = axes[0]
ax1 = axes[1]
ax2 = axes[2]

sns.boxplot(
    ax=ax, 
    data=churn_data, 
    y='Exited', 
    x='Age', 
    orient='h', 
    palette=[colors[0], colors[1]]
)

#ax.set_yticks([1, 0])
ax.set_yticklabels(['Лояльные', 'Ушедшие'], fontsize=12, rotation=90, va='center')

ax.set_title('Соотношение', fontsize=14)
ax.set_xlabel('Возраст', fontsize=12)
ax.set_ylabel('')


ax1.hist(churn_data[churn_data['Exited'] == 0]['Age'], color=colors[1])
ax1.set_title('Лояльные', fontsize=14)


ax2.hist(churn_data[churn_data['Exited'] == 1]['Age'], color=colors[0])
ax2.set_title('Ушедшие', fontsize=14)

#plt.show()


# 9.5. Постройте график, который показывает взаимосвязь кредитного рейтинга клиента и его предполагаемой зарплаты. 
# Добавьте расцветку по признаку оттока клиентов. 
# Какова взаимосвязь между признаками? Если не видите явной взаимосвязи, укажите это.
fig = plt.figure('9.5', figsize=figsize2)
ax = fig.add_axes([0,0,1,1])

sns.scatterplot(
    ax=ax, 
    data=churn_data, 
    x='EstimatedSalary', 
    y='CreditScore', 
    hue='Exited', 
    palette='pastel'
)

ax.get_xticks(minor=False)
ax.set_xticklabels([f"{round(x)}K" for x in ax.get_xticks()/1000])

ax.set_title('Взаимосвязь кредитного рейтинга от предполагаемой з/п', fontsize=18)
ax.set_xlabel('Предполагаемая з/п', fontsize=14)
ax.set_ylabel('Кредитный рейтинг', fontsize=14)

ax.legend(title='Статус клиента', labels=['Ушедший', 'Лояльный'])
ax.grid(True);


# 9.6. Кто чаще уходит, мужчины или женщины? Постройте график, который иллюстрирует это.
# Процент ушедших клиентов в каждой группе можно рассчитать как среднее по столбцу Exited 
# (так как 1 — это ушедшие клиенты, а 0 — лояльные, среднее арифметическое по столбцу обозначает долю ушедших клиентов).
male_female = churn_data.copy()[['Gender', 'Exited']]                                           # Создаем таблицу со столбцами 'Gender', 'Exited'
male_female['Status'] = male_female['Exited'].apply(lambda x: 'Loyal' if x == 0 else 'Exited')  # Добавляем признак Статус клиента
gender_groups = male_female.groupby('Gender')['Exited'].count().reset_index()                   # Считаем отдельно сколько мужчин и женщин
gender_status = male_female.groupby(['Gender', 'Status'])['Exited'].count().reset_index()       # Распределяем статус клиента по гендерному признаку 
gender_status.loc[2], gender_status.loc[3] = gender_status.loc[3], gender_status.loc[2]         # Переставляем части пирога для более красивого отображения


fig = plt.figure('9.6', figsize=figsize2)
fig.subplots_adjust(top=0.8)
fig.suptitle('Соотношение мужчин и женщин', fontsize=18)
axes = fig.subplots(1, 2)

axes[0].pie(
    gender_groups.Exited,
    labels=['Женщины', 'Мужчины'], 
    autopct='%1.1f%%',
    textprops={'fontsize': 12},
    startangle=0,
    colors=[colors[6], colors[0]]
)

axes[0].set_title('Гендерное соотношние', fontsize=14)
axes[1].set_title('Отдельно лояльные и ушедшие', fontsize=14)

axes[1].pie(
    gender_status.Exited,
    explode=[0.1, 0, 0, 0.1], 
    labels=['Ушедшие', 'Женщины', 'Мужчины', 'Ушедшие'], 
    autopct='%1.1f%%',          # Отображение доли в процентах
    textprops={'fontsize': 11},
    startangle=0,
    colors=[colors[6], colors[6], colors[0], colors[0]]
);

# Коэффицент утечки женщин
k = 100 / 45.4
r = 11.4 * k
k_female = 100 / r
print('Каждая {0}-ая женщина уходит из банка.'.format(round(k_female)))


# Коэффицент утечки мужчин
k2 = 100 / 54.6
r2 = 9 * k2
k_male = 100 / r2
print('Каждый {0}-ой мужчина уходит из банка.'.format(round(k_male)))


# 9.7. Как отток клиентов зависит от числа приобретённых у банка услуг? 
# Для ответа на этот вопрос постройте многоуровневую столбчатую диаграмму.
fig = plt.figure('9.7', figsize=figsize2)
fig.subplots_adjust(top=0.8)
fig.suptitle('Зависимость оттока клиентов от кол-ва приобретенных услуг', fontsize=18)

axes = fig.subplots(1, 2)         # Два фрейма в одну строку
ax = axes[0]

sns.barplot(
    ax=ax,
    data=churn_data,
    x='NumOfProducts',
    y='CustomerId',
    hue='Exited',                   # Указываем какой столбец во фрейме данных следует использовать для кодирования цвета
    estimator=len,                  # Подсчитываем фактическое кол-во элементов.
    palette=[colors[0], colors[1]],
)

handles, labels = ax.get_legend_handles_labels()  # Создаем переменные для легенды
labels = ['Лояльный', 'Ушедший']                   # Руссифицируем категории клиентов
ax.set_title('Потребление в разрезе статуса', fontsize=14)
ax.set_ylabel('Кол-во клиентов, чел.', fontsize=14)
ax.set_xlabel('Когорты набора услуг')
ax.legend(handles, labels, title='Статус клиента')

# Делаем выборку по кол-ву приобретенных услуг и статуса лояльности
purchased_services = pd.DataFrame([churn_data.groupby('NumOfProducts')['Exited'].count()])

ax2 = axes[1]

sns.barplot(
    ax=ax2, 
    data=purchased_services, 
    palette=[colors[4], colors[5], colors[2], colors[3]]
)

ax2.set_title('Общее потребление услуг', fontsize=14)
ax2.set_xlabel('Когорты набора услуг');

#plt.show()


# 9.8. Как влияет наличие статуса активного клиента на отток клиентов? 
active_inactive = churn_data.copy()[['IsActiveMember', 'Exited']]                                       # Делаем выборку Статус клиента и его данные активности 
active_inactive['Status'] = active_inactive['Exited'].apply(lambda x: 'Loyal' if x == 0 else 'Exited')  # Добавляем новый признак статус клиента
active_inactive.rename(columns={'Exited': 'Count'}, inplace=True)                                       # Переименовываем столбец который используется в роли счетчика

data1 = active_inactive.groupby('IsActiveMember')['Count'].count().reset_index()                        # Группируем и подсчитываем кол-во активных клиентов

data2 = active_inactive.groupby(['IsActiveMember', 'Status'])['Count'].count().reset_index()   # Группируем и подсчитываем лояльных и ушедших клиентов
data2.loc[2], data2.loc[3] = data2.loc[3], data2.loc[2]                                         # Меняем местами доли пирога для более удобного отображения

fig = plt.figure('9.8', figsize=figsize2)
fig.subplots_adjust(top=0.8)
fig.suptitle('Соотношение активных и неактивных клиентов', fontsize=18)
axes = fig.subplots(1, 2)

axes[0].pie(
    data1.Count,
    labels=['Неактивные', 'Активные'], 
    autopct='%1.1f%%',
    textprops={'fontsize': 12},
    startangle=0,
    colors=[colors[7], colors[2]]
)

axes[0].set_title('Общий вклад', fontsize=14)
axes[1].set_title('Отдельно лояльные и ушедшие', fontsize=14)

axes[1].pie(
    data2.Count,
    explode=[0.1, 0, 0, 0.1], 
    labels=['Неакт. ушедшие', 'Неакт. лояльные', 'Акт. лояльные', 'Акт. ушедшие'], 
    autopct='%1.1f%%',
    textprops={'fontsize': 12},
    startangle=0,
    colors=[colors[7], colors[7], colors[2], colors[2]]
);


# 9.9. В какой стране доля ушедших клиентов больше? 
# Постройте тепловую картограмму, которая покажет это соотношение на карте мира. 
# Предположите, с чем это может быть связано.
ch = churn_data[['Geography', 'Exited']]                                        # Формируем список стран
ch = ch.groupby('Geography').agg(['count', 'sum']).reset_index()                # Суммируем кол-во ушедших в столбце sum
ch['ExitedPercent'] = round(ch['Exited']['sum'] / ch['Exited']['count'] * 100)  # Вычисляем процент ушедших
ch.rename(columns={'ExitedPercent': 'Процент ушедших', 'Geography': 'Страна'}, inplace=True)# Переименовываем для корректного отображения на графике

fig = px.choropleth(
    data_frame=ch,
    locations='Страна',
    locationmode = 'country names',
    color='Процент ушедших',
    range_color=[0, 50],
    title='География распределения ушедших клиентов',
    width=600,
    height=400,
    color_continuous_scale='Reds',
    scope='europe',
)

#fig.show();


# 9.10. Переведите числовой признак CreditScore в категориальный. 
# Примените функцию get_credit_score_cat() к столбцу CreditScore 
# и создайте новый признак CreditScoreCat — категории кредитного рейтинга.
def get_credit_score_cat(credit_score):
    if credit_score >= 300 and credit_score < 500:
        return "Very_Poor"
    elif credit_score >= 500 and credit_score < 601:
        return "Poor"
    elif credit_score >= 601 and credit_score < 661:
        return "Fair"
    elif credit_score >= 661 and credit_score < 781:
        return "Good"
    elif credit_score >= 851:
        return "Top"
    elif credit_score >= 781 and credit_score < 851:
        return "Excellent"
    elif credit_score < 300:
        return "Deep"


ch = churn_data.copy()                                                # Копируем из основного датасета в переменную для последующей трансформации
ch['CreditScoreCat'] = ch['CreditScore'].apply(get_credit_score_cat)  # Создаем новый признак Категория кредитного рейтинга.Заполняем примененяя функцию
ch['CreditScoreCat'] = ch['CreditScoreCat'].astype('category')

summary_table = ch.pivot_table(
    index='CreditScoreCat',     # категории кредитного рейтинга (CreditScoreCat)
    columns='Tenure',           # количество лет, в течение которых клиент пользуется услугами банка (Tenure)
    values='Exited',            # Статус клиента
    aggfunc='mean',             # В ячейках сводной таблицы должно находиться среднее по признаку оттока (Exited) — доля ушедших пользователей.
)

fig = plt.figure('9.10', figsize=figsize2)
fig.subplots_adjust(top=0.75)
fig.suptitle('Тренд оттока клиентов в разрезе\n\
кредитного рейтинга и продолжительности использвания услуг банка', fontsize=16)

axes = fig.subplots(1, 2)             # Указывем кол-во строк и кол-во графиков в строке
ax = axes[0]
ax2 = axes[1]

# На основе полученной сводной таблицы постройте тепловую карту с аннотацией. 
# Найдите на тепловой карте категории клиентов, которые уходят чаще всего.
sns.heatmap(
    ax=ax,
    data=summary_table,
    annot=True,
    annot_kws={'size': 7},
    cmap=sns.light_palette(colors[1])
)

ax.set_title('Среднее по признаку оттока', fontsize=14)

ax.set_ylabel('Категория кредитного рейтинга', fontsize=12)
ax.set_yticklabels(ax.get_yticklabels(), rotation=60) # Меняем отображение категорий рейтинга под углом
ax.set_xlabel('Использование услуг, лет', fontsize=11)


summary_table_2 = ch.pivot_table(
    index='CreditScoreCat',       # категории кредитного рейтинга (CreditScoreCat)
    columns='Tenure',             # количество лет, в течение которых клиент пользуется услугами банка (Tenure)
    values='Exited',              # Данные берём из столбца со статусами клиентов
    aggfunc='count',              # График строим опираясь на кол-во клиентов
)

sns.heatmap(
    ax=ax2,
    data=summary_table_2,
    cmap=sns.light_palette(colors[5])
)

ax2.set_title('Распределение категорий рейтинга', fontsize=14)
ax2.set_ylabel('')
ax2.set_yticklabels(ax.get_yticklabels(), rotation=60)
ax2.set_xlabel('Использование услуг, лет', fontsize=11);

#plt.show()


summary_table_4 = ch.copy()[['CreditScoreCat', 'Exited']]                                   # Делаем выборку категория рейтинга и статус клиента
summary_table_4['Status'] = summary_table_4['Exited'].apply(lambda x: 'Loyal' if x == 0 else 'Exited')  # Добавляем новый признак статус клиента
summary_table_4.rename(columns={'Exited': 'Count'}, inplace=True)                           # Переименовываем столбец который теперь счетчик статусов
data3 = summary_table_4.groupby(['CreditScoreCat', 'Status'])['Count'].count().reset_index()# На основании выборки делаем необходимые группировки

fig = plt.figure('9.10.1', figsize=(10, 8))
fig.subplots_adjust(top=0.9)
fig.suptitle('Соотношение лояльных и ушедших \n в разрезе кредитного рейтинга и общего кол-ва клиентов', fontsize=16)
axes = fig.subplots(1, 1)

axes.pie(
    data3.Count,
    explode=[0.1, 0, 0.1, 0, 0.1, 0, 0.1, 0, 0.1, 0],                           # Акцентируем долю ушедших
    labels=['Ушедший', 'Максимальный', 'Ушедший', 'Выше среднего', 'Ушедший', 'Средний', 'Ушедший', 'Низкий', 'Ушедший', 'Очень низкий'], 
    autopct='%1.1f%%',
    textprops={'fontsize': 12},
    #startangle=0,
    colors=['red', 'red', 'green', 'green', colors[2], colors[2], colors[5], colors[5], colors[7], colors[7]]
);

plt.show()

# Шпаргалки
# Суммы по годам
# print(summary_table_2.iloc[:, :].sum())
# print(summary_table_2[:][:].sum())
# суммировать конкретную строку 
# print(summary_table_2.loc['Excellent'].sum())