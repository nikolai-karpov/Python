import pandas as pd
import matplotlib.pyplot as plt

covid_data = pd.read_csv('data/covid_data.csv')


"""
Мы будем работать со следующими столбцами:

date — дата наблюдения;
province/state — наименование провинции/штата;
country — наименование страны;
confirmed — общее число зафиксированных случаев на указанный день;
deaths — общее число зафиксированных смертей на указанный день;
recovered — общее число выздоровлений на указанный день.
"""


vaccinations_data = pd.read_csv('data/country_vaccinations.csv')
vaccinations_data = vaccinations_data[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]


"""
Данная таблица содержит следующие столбцы:

country — наименование страны;
date — дата наблюдения;
total_vaccinations — общее число введённых вакцин в стране на указанный день;
people_vaccinated — общее число привитых первым компонентом в стране на указанный день;
people_vaccinated_per_hundred — процент привитых первым компонентом в стране на указанный день (рассчитывается как people_vaccinated/population*100);
people_fully_vaccinated — общее число привитых вторым компонентом в стране на указанный день (первый компонент уже был введён им ранее);
people_fully_vaccinated_per_hundred — процент привитых вторым компонентом в стране на указанный день (рассчитывается как people_fully_vaccinated/population*100);
daily_vaccination — ежедневная вакцинация (число вакцинированных в указанный день);
vaccines — комбинации вакцин, используемые в стране.
"""


# Группируем таблицу по дате и названию страны и рассчитываем суммарные показатели по всем регионам
covid_data = covid_data.groupby(
    ['date', 'country'], 
    as_index=False
)[['confirmed', 'deaths', 'recovered']].sum()


# Преобразуем даты в формат datetime с помощью функции pd.to_datetime():
covid_data['date'] = pd.to_datetime(covid_data['date'])


# Создадим признак больных на данный момент (active). 
# Для этого вычтем из общего числа зафиксированных случаев число смертей и число выздоровевших пациентов:
covid_data['active'] = covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered']


# Создадим признак ежедневного прироста числа заболевших, умерших и выздоровевших людей
covid_data = covid_data.sort_values(by=['country', 'date'])                         # отсортируем данные по названиям стран, а затем по датам
covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()   # произведём группировку по странами и рассчитаем разницу между «вчера и сегодня»
covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()
covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()


# В таблице vaccinations_data преобразовать столбцы в формат datetime:
vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])


# За какой период представлены данные covid_data
print(f"Данные о заболеваемости предоставлены от {covid_data['date'].min()} до  {covid_data['date'].max()}")


# За какой период представлены данные в таблице vaccinations_data?
print(f"Данные о заболеваемости предоставлены от {vaccinations_data['date'].min()} до  {vaccinations_data['date'].max()}")


# С помощью метода merge() объедините таблицы covid_data и vaccinations_data по столбцам date и country.
# Тип объединения выставьте так, чтобы в результирующую таблицу попали только наблюдения за период 2020-01-22 2021-05-29. 
# То есть в результирующую таблицу должны попасть все записи из таблицы covid_data и из её пересечения с vaccinations_data, но не более. 
# Результат объединения занесите в переменную covid_df.
covid_df = covid_data.merge(vaccinations_data, on=['date', 'country'], how='left')

print('Число строк: ', covid_df.shape[0])
print('Число столбцов: ', covid_df.shape[1])


# В таблице covid_df создайте признаки death_rate — общий процент смертей среди зафиксированных случаев (летальность) 
# и recover_rate — общий процент случаев выздоровления
covid_df['death_rate'] = (covid_df['deaths'] / covid_df['confirmed'])*100
covid_df['recover_rate'] =  (covid_df['recovered'] / covid_df['confirmed'])*100


# Какова максимальная летальность в США (United States) за весь период? 
# Ответ округлите до второго знака после запятой.
print(round(covid_df[covid_df['country'] == 'United States']['death_rate'].max(), 2))


# Чему равен средний процент выздоровевших в России (Russia)? 
# Ответ округлите до второго знака после запятой.
print(round(covid_df[covid_df['country'] == 'Russia']['recover_rate'].mean(), 2))


# БАЗОВАЯ ВИЗУАЛИЗАЦИЯ В PANDAS
# Основным методом для создания простейших графиков в Pandas является plot().
"""
x — название признака, который будет отложен по оси абсцисс;
y — название признака, который будет отложен по оси ординат;

figsize — размер графика (кортеж из ширины и высоты в дюймах);
grid — отображение сетки (по умолчанию False);
legend — отображение легенды (по умолчанию False);
title — название графика;
color — цвет

kind — тип визуализации. 
Основные типы:
    'line' — линейный график (по умолчанию);
    'bar' — столбчатая диаграмма;
    'barh' — горизонтальная столбчатая диаграмма;
    'hist' — гистограмма;
    'box' — коробчатая диаграмма (boxplot);
    'pie' — круговая диаграмма;
    'scatter' — диаграмма рассеяния.
   
"""


# как менялось ежедневное число заболевших (daily_confirmed) во всём мире во времени
# сгруппируем таблицу по датам и подсчитаем суммарное число зафиксированных случаев по дням.
grouped_cases = covid_df.groupby('date')['daily_confirmed'].sum()

# построить график с помощью метода plot().
"""
grouped_cases.plot(
    kind='line',                                        # линейный график
    figsize=(12, 4),                                    # размером 12x4
    title='Ежедневная заболеваемость по всем странам',  # Подпишем график
    grid = True,                                        # отобразим сетку
    lw=3                                                # (line width) отвечает за ширину линии для линейного графика.
);


# С помощью перечисленных ниже вариантов кода можно получить график
grouped_cases = covid_df.groupby('date')['daily_deaths'].sum()
grouped_cases.plot(kind='line',xlabel='Дата', ylabel='Число смертей в мире');


# построить столбчатую диаграмму для пяти стран с наименьшим общим числом вакцинаций на последний день рассматриваемого периода (total_vaccinations)
#  метод nsmallest(), который позволяет выбрать n наименьших значений в Series
covid_df.groupby(['country'])['total_vaccinations'].last().nsmallest(5).plot(kind='bar', title='страны с наименьшим общим числом вакцинаций');

"""

# ОСНОВНЫЕ ОБЪЕКТЫ MATPLOTLIB

fig = plt.figure(figsize=(8, 4))    # создаётся объект фигуры, размер в дюймах figsize: восемь дюймов в ширину, четыре — в высоту
axes = fig.add_axes([0, 0, 1, 1])   # с помощью метода add_axes() добавляется координатная плоскость


# Для создания координатной плоскости необходимо указать её расположение на фигуре в виде списка из координат. 
# В нашем случае она начинается в левом нижнем углу без отступов (координаты 0, 0) 
# и занимает всё отведённое место в области (100%, ширина и высота равны 1).


# Основные параметры метода scatter()
"""
x, y — последовательности, которые будут отложены по осям абсцисс и ординат;
s — размер маркеров;
marker — вид маркеров ('o' — точки, '^' — треугольники);
c — цвет маркеров.
"""

# У объекта координатной плоскости axes вызовем метод scatter().
us_data = covid_df[covid_df['country'] == 'United States']

fig = plt.figure(figsize=(8, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.scatter(
    x=us_data['people_fully_vaccinated'],   # откладываем суммарное число поставленных вакцин
    y=us_data['daily_confirmed'],           # ежедневный прирост заболевших
    s=100,
    marker='o',
    c = 'blue'
);



# Для построения круговых диаграмм в Matplotlib используется метод pie().
"""
Основные параметры метода pie()
x — значения, по которым будет строиться круговая диаграмма;
labels — метки, соответствующие значениям;
autopct — формат отображения долей на диаграмме (например, '%.1f%%' означает, что округление будет производиться до первого знака после запятой и при выводе будет указан знак "%"; открывающий и закрывающий проценты означают форматирование, а внутренний — вывод знака "%");
explode — последовательность, которая определяет долю смещения сектора от центра для каждого значения из x.
"""


# ТОП-10 комбинаций вакцин (vaccines) по распространённости
vaccine_combinations = covid_df['vaccines'].value_counts()[:10]
fig = plt.figure(figsize=(5, 5))
axes = fig.add_axes([0, 0, 1, 1])
axes.pie(
    vaccine_combinations,
    labels=vaccine_combinations.index,          # метки для каждого значения — индексы промежуточной таблицы
    autopct='%.1f%%',                           # Будем отображать доли в процентах и округлять их до одного знака после запятой
    explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Самую распространённую вакцину сместим на 10 % от центра
);


# выделить каждую вакцину в отдельности и посчитать, в скольки странах она используется.
# необходимо избавиться от пропусков в столбце с вакцинами
combination_not_nan = covid_df.dropna(subset=['vaccines'])


# сгруппировать по странам (country) и определить последнюю зафиксированную комбинации вакцин в столбце vaccines:
# получаем комбинации вакцин, которые использовались в странах в последний день рассматриваемого периода
combination_last = combination_not_nan.groupby(['country'])['vaccines'].last()


# Преобразуем данные 
# будем удалять из строки с комбинациями вакцин пробелы и разделять комбинацию на отдельные составляющие по запятым.
vaccines_unique = combination_last.apply(lambda x: x.replace(' ', '').split(','))


# Создадим словарь, ключами которого будут являться уникальные вакцины, 
# а значениями — количество стран, в которых они используются. 
# Изначально словарь пустой.
vaccines_dict = {} 
#создаём цикл по элементам Series combination_last
for vaccines_list in combination_last:      #создаём цикл по элементам списка с вакцинами
    # в переменной цикла vaccines_list будет находиться список вакцин, которые используются в стране.
    for vaccine in vaccines_list:
        #проверяем условие, что текущей вакцины ещё нет среди ключей словаря
        if vaccine not in vaccines_dict:    # если условие выполняется
            vaccines_dict[vaccine] = 1      # заносим вакцину в словарь со значением 1
        else: #в противном случае
            vaccines_dict[vaccine] += 1     #увеличивает количество
            

vaccines = pd.Series(vaccines_dict).sort_values(ascending=False)    # получаем словарь, который преобразуем в объект Series
vaccines['other'] = vaccines[7:].sum()                              # Вычислим суммарное количество стран, в которых используются вакцины, не попавшие в наш ТОП-7, результат запишем в Series по индексу 'other'.
                                                                    # выделим семь наиболее популярных вакцин, а остальные обозначим как 'other'
vaccines = vaccines.sort_values(ascending=False)[:8]                # выделим восемь наибольших значений в полученной Series — для них и будем строить круговую диаграмму.

fig = plt.figure(figsize=(5, 5))
axes = fig.add_axes([0, 0, 1, 1])
axes.pie(
    vaccines,
    labels=vaccines.index,
    autopct='%.1f%%',
);


# ДОБАВЛЕНИЕ ИНФОРМАТИВНОСТИ В ГРАФИКИ
"""
axes.set_title() — заголовок диаграммы, а также его настройки (например, параметр fontsize отвечает за размер шрифта);
axes.set_xlabel() — название оси абсцисс;
axes.set_ylabel() — название оси ординат;
axes.set_xticks() — установка отметок на оси абсцисс;
axes.set_yticks() — установка отметок на оси ординат;
axes.xaxis.set_tick_params() — управление параметрами отметок на оси абсцисс (например, параметр rotation отвечает за поворот отметок в градусах);
axes.yaxis.set_tick_params() — управление параметрами отметок на оси ординат;
axes.legend() — отображение легенды;
axes.grid() — установка сетки.
"""


# как росла общая заболеваемость (confirmed), число зафиксированных смертей (deaths), выздоровевших пациентов (recovered) и активных случаев (active) в Китае.
china_data = covid_df[covid_df['country'] == 'China']
china_grouped = china_data.groupby(['date'])[['confirmed', 'active', 'deaths', 'recovered']].sum()

#визуализация графиков
fig = plt.figure(figsize=(10, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.plot(china_grouped['confirmed'], label='Общее число зафиксированных случаев', lw=3)    # lw — ширина линии графика
axes.plot(china_grouped['deaths'], label='Общее число смертей', lw=3)
axes.plot(china_grouped['recovered'], label='Общее число выздоровевших пациентов', lw=3)
axes.plot(china_grouped['active'], label='Общее число активных случаев', lw=3, linestyle='dashed')

#установка параметров отображения
axes.set_title('Статистика Covid-19 в Китае', fontsize=16)
axes.set_xlabel('Даты')
axes.set_ylabel('Число случаев')
axes.set_yticks(range(0, 100000, 10000))    # установим метки по оси y с частотой в 10 000
axes.xaxis.set_tick_params(rotation=30)     # повернём метки по оси x на 30 градусов
axes.grid()
axes.legend();


# ИСПОЛЬЗОВАНИЕ НЕСКОЛЬКИХ СИСТЕМ КООРДИНАТ
# Для добавления второй системы координат необходимо повторно применить к объекту fig метод add_axes, 
# указав новое имя для второй системы координат.


# отобразим ТОП-5 стран по общему числу привитых вторым компонентом людей (people_fully_vaccinated), 
# а также ТОП-5 стран по числу полностью привитых на 100 человек населения (people_fully_vaccinated_per_hundred).

# столбчатые диаграммы с помощью метода bar()
"""
Основные параметры метода bar():
x       — названия категорий, которые будут располагаться по оси абсцисс;
height  — высота столбцов диаграммы, массив из показателей для визуализации (например, среднее, максимальное значение и т. д.);
width   — ширина столбцов диаграммы;
color   — цвет.
"""


# Группируем таблицу по странам, находим последний по дате зафиксированный показатель с помощью метода last() 
# и выбираем ТОП-5 стран с использованием метода nlargest().
vacc_country = covid_df.groupby('country')['people_fully_vaccinated'].last().nlargest(5)
vacc_country_per_hundred = covid_df.groupby('country')['people_fully_vaccinated_per_hundred'].last().nlargest(5)

# При отображении графиков создаём две координатные плоскости main_axes и insert_axes, 
# на каждой из них отдельно строим столбчатые диаграммы.
# визуализация главного графика
fig = plt.figure(figsize=(13, 4))
main_axes = fig.add_axes([0, 0, 1, 1])  # Первые два числовых параметра, указанные при создании систем координат, — это отступ снизу и слева, 
                                        # следующие два — ширина и высота относительно ширины и высоты всего пространства 
                                        # (в долях единицы) для построения графика.
main_axes.bar(x = vacc_country.index, height = vacc_country);
main_axes.set_ylabel('Число вакцинированных (2 компонент)')
main_axes.set_title('Топ 5 стран по числу полностью привитых людей')

# визуализация вспомогательного графика
insert_axes = fig.add_axes([0.6, 0.6, 0.38, 0.38])
insert_axes.bar(x = vacc_country_per_hundred.index, height = vacc_country_per_hundred, width=0.5);
insert_axes.set_ylabel('На 100 человек')
insert_axes.xaxis.set_tick_params(rotation=45)


# SUBPLOTS
# используется для отображения нескольких систем координат 
"""
    Основные параметры метода subplots()
nrows — число строк;
ncols — число столбцов;
figsize — общий размер фигуры в дюймах (ширина и высота).
"""


# За построение гистограмм в библиотеке Matplotlib отвечает метод hist()
"""
Основные параметры метода hist()
x — массив чисел, для которого строится гистограмма;
bins — число столбцов (корзин);
orientation — ориентация гистограммы (по умолчанию 'vertical');
color — цвет.
"""


russia_data = covid_df[covid_df["country"] == "Russia"] # Фильтруем таблицу covid_df по признаку страны и выбираем записи только для России.

# визуализация систем координат
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))

# столбчатая диаграмма
axes[0].bar(    # Для того чтобы отобразить график в соответствующей координатной плоскости, нужно обратиться по индексу (от 0 до 2).
    x=russia_data["date"],
    height=russia_data["daily_vaccinations"],
    label="Число вакцинированных",
)
axes[0].set_title("Ежедневная вакцинация в России")
axes[0].xaxis.set_tick_params(rotation=45)

# линейный график
axes[1].plot(
    russia_data["date"],
    russia_data["daily_confirmed"],
    label="Число заболевших",
    color="tomato",
    lw=2,
)
axes[1].set_title("Ежедневная заболеваемость в России")
axes[1].xaxis.set_tick_params(rotation=45)

# гистограмма
axes[2].hist(
    x=russia_data["daily_confirmed"], label=["Число заболевших"], color="lime", bins=20
)
axes[2].set_title("Гистограмма заболеваемости в России")
axes[2].xaxis.set_tick_params(rotation=30)


# Раскрашивание внешнего периметра графика
fig = plt.figure(facecolor='lightgreen')
axes = fig.add_axes([0, 0, 1, 1])
axes.hist(covid_df.groupby('date')['daily_vaccinations'].sum())
axes.set_ylabel('Ежедневная вакцинация в мире');


import seaborn as sns
# print(sns.__version__)


countries = ['Russia', 'Australia', 'Germany', 'Canada', 'United Kingdom']
croped_covid_df = covid_df[covid_df['country'].isin(countries)] # проверяет, есть ли запись в столбце в переданном в метод списке. 
                                                                # В результате возвращается привычная нам маска.

populations = pd.DataFrame([
    ['Canada', 37664517],
    ['Germany', 83721496],
    ['Russia', 145975300],
    ['Australia', 25726900],
    ['United Kingdom', 67802690]
    ],
    columns=['country', 'population']
)
croped_covid_df = croped_covid_df.merge(populations, on=['country'])
croped_covid_df['daily_confirmed_per_hundred'] = croped_covid_df['daily_confirmed'] / croped_covid_df['population'] * 100   # рассчитать ежедневную заболеваемость на 100 человек
                                                                                                                            # заболеваемость в процентах от общего количества населения

# БИБЛИОТЕКА Seaborn 
# pairplot(), который позволяет строить матрицу из диаграмм рассеяния для всех пар числовых признаков, а на диагонали этой матрицы отображаются гистограммы.
# С помощью параметра hue в графиках Seaborn можно группировать данные по признаку и отображать каждую категорию разным цветом


# Гистограммы
"""
Основные параметры метода histplot():
data — DataFrame, по которому строится график;
x — признак, который будет отложен по оси абсцисс;
y — признак, который будет отложен по оси ординат;
hue — группировочный категориальный признак, который позволяет строить отдельный график для каждой категории (не стоит использовать его для гистограмм, но он широко используется для других видов графиков в Seaborn);
ax — система координат Matplotlib, в которой строится график;
color — цвет графика;
bins — число столбцов в гистограмме (по умолчанию вычисляется автоматически с помощью специальных формул);
kde — параметр, указывающий, стоит ли сглаживать гистограмму кривой (по умолчанию False). 
"""

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))
sns.histplot(
    data=croped_covid_df,
    x='daily_confirmed_per_hundred',
    bins=25,
    kde=True,
    ax=axes[0]
);
axes[0].set_title('Гистограмма ежедневной заболеваемости на 100 человек', fontsize=16)
sns.histplot(
    data=croped_covid_df,
    x='daily_confirmed_per_hundred',
    y='country',
    bins=25,
    color='red',
    ax=axes[1]
);

# Коробчатые диаграммы в Seaborn строятся с помощью метода boxplot().
fig = plt.figure(figsize=(10, 7))
boxplot = sns.boxplot(
    data=croped_covid_df,
    y='country',
    x='death_rate',
    orient='h',     # параметр orient отвечает за ориентацию диаграммы
    width=0.9       # параметр width — за ширину коробок
)
boxplot.set_title('Распределение летальности по странам');
boxplot.set_xlabel('Летальность');
boxplot.set_ylabel('Страна');
boxplot.grid()


# Для построения столбчатых диаграмм в Seaborn используется метод barplot()
fig = plt.figure(figsize=(10, 7))
croped_covid_df['quarter'] = croped_covid_df['date'].dt.quarter
barplot = sns.barplot(
    data=croped_covid_df,
    x='country',
    y='daily_confirmed_per_hundred',
    hue='quarter',                  # Для добавления многоуровневости
)
barplot.set_title('Средний процент болеющего населения по кварталам');


# диаграмма рассеяния и гистограмма
# когда мы хотим одновременно посмотреть и на распределения переменных, и сразу оценить их взаимосвязь.
jointplot = sns.jointplot(
    data=croped_covid_df, 
    x='people_fully_vaccinated_per_hundred', 
    y='daily_confirmed_per_hundred',
    hue='country',
    xlim = (0, 40),     # определяют диапазон отображения ось x
    ylim = (0, 0.1),    # определяют диапазон отображения ось y
    height=8,           # отвечает за высоту и ширину графика (он квадратный).
)


# тепловая карта.
# Предварительно создадим сводную таблицу
pivot = croped_covid_df.pivot_table(
    values='people_vaccinated_per_hundred',
    columns='date',
    index='country',
)
pivot.columns = pivot.columns.astype('string')


# Для построения тепловой карты в Seaborn используется метод heatmap()
# annot отвечает за отображение легенды (аннотации)
heatmap = sns.heatmap(data=pivot, cmap='YlGnBu')    # cmap отвечает за цветовую гамму графика
heatmap.set_title('Тепловая карта вакцинации', fontsize=16);


# Создайте новый признак confirmed_per_hundred, который покажет процентное отношение заболевших вирусом к общему числу населения в странах ().
croped_covid_df['confirmed_per_hundred'] = croped_covid_df['confirmed']/croped_covid_df['population'] * 100

# Постройте тепловую карту, 
# Предварительно создадим сводную таблицу
pivot = croped_covid_df.pivot_table(
    values='confirmed_per_hundred',
    columns='date',
    index='country',
)
pivot.columns = pivot.columns.astype('string')
# которая покажет, как росло число заболевших в процентах от общего числа населения (confirmed_per_hundred) в странах из таблицы croped_covid_df.
fig = plt.figure(figsize=(10, 5))
                 
heatmap = sns.heatmap(data=pivot, cmap='plasma')    # cmap отвечает за цветовую гамму графика
heatmap.set_title('Тепловая карта заболеваемости', fontsize=16);


# Постройте коробчатую диаграмму для признака recover_rate (отношение выздоровлений к числу зафиксированных случаев заболевания в процентах).
fig = plt.figure(figsize=(10, 7))
boxplot = sns.boxplot(
    data=croped_covid_df,
    y='recover_rate',
    x='country',
    orient='v',     # параметр orient отвечает за ориентацию диаграммы
    width=0.9       # параметр width — за ширину коробок
)
boxplot.set_title('Распределение по странам');
boxplot.set_xlabel('% Выздоровивших');
boxplot.set_ylabel('Страны');
boxplot.grid()



#plt.show()