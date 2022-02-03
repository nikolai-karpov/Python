# Графические возможности библиотеки Plotly

import plotly
import plotly.express as px

#print(plotly.__version__)

"""
line() — линейные графики;
histogram() — гистограммы;
scatter() — диаграммы рассеяния;
box() — коробчатые диаграммы;
bar() — столбчатые диаграммы;
pie() — круговые диаграммы.
"""

import pandas as pd
covid_data = pd.read_csv('data/covid_data.csv')
vaccinations_data = pd.read_csv('data/country_vaccinations.csv')
vaccinations_data = vaccinations_data[
    ['country', 'date', 'total_vaccinations', 
     'people_vaccinated', 'people_vaccinated_per_hundred',
     'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
     'daily_vaccinations', 'vaccines']
]
covid_data = covid_data.groupby(
    ['date', 'country'], 
    as_index=False
)[['confirmed', 'deaths', 'recovered']].sum()
covid_data['date'] = pd.to_datetime(covid_data['date'])
covid_data['active'] = covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered']
covid_data = covid_data.sort_values(by=['country', 'date'])                         # отсортируем данные по названиям стран, а затем по датам
covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()   # произведём группировку по странами и рассчитаем разницу между «вчера и сегодня»
covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()
covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()
vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])
covid_df = covid_data.merge(vaccinations_data, on=['date', 'country'], how='left')
covid_df['death_rate'] = (covid_df['deaths'] / covid_df['confirmed'])*100
covid_df['recover_rate'] =  (covid_df['recovered'] / covid_df['confirmed'])*100


# ЭКСПРЕСС-РЕЖИМ


# Основные параметры метода line()
"""
data_frame — DataFrame, по которому строится график;
x — признак по оси абсцисс;
y — признак по оси ординат;
height — высота графика;
width — ширина графика;
title — название графика.
"""


# График роста зафиксированного числа случаев заражения (confirmed), смертей (deaths), выздоровлений (recovered) и активных случаев (active) за всё время. 
# Для этого просуммируем статистику по дням и передадим полученный DataFrame в метод line().
line_data = covid_df.groupby('date', as_index=False).sum()  # Сброс индекса as_index=False
fig = px.line(
    data_frame=line_data,                               # DataFrame
    x='date',                                           # ось абсцисс
    y=['confirmed', 'recovered', 'deaths', 'active'],   # ось ординат
    height=500,                                         # высота
    width=1000,                                         # ширина
    title='Confirmed, Recovered, Deaths, Active cases over Time' # заголовок
)


# Постройте линейный график, который отображает, как изменялось ежедневное количество вакцинированных (daily_vaccinations) в мире во времени. 
# Из графика найдите, чему равно количество вакцинированных (в миллионах) 28 февраля 2021 года (2021-02-28).
line_data = covid_df.groupby('date', as_index=False).sum()  # Сброс индекса as_index=False
fig = px.line(
    data_frame=line_data,                               # DataFrame
    x='date',                                           # ось абсцисс
    y=['daily_vaccinations'],                           # ось ординат
    height=500,                                         # высота
    width=1000,                                         # ширина
    title='Daily vaccinations over Time'                # заголовок
)


# Столбчатая диаграмма

# ТОП-10 стран по среднему проценту выздоравливающих пациентов (recover_rate)
# используем метод bar() модуля express
"""
color — группирующий признак, в соответствии с которым будут раскрашены столбцы диаграммы;
text — текст, который будет подписан на столбцах диаграммы;
orientation — ориентация графика ('v' — вертикальная, 'h' — горизонтальная).
"""
#считаем средний процент выздоровлений для каждой страны
bar_data = covid_df.groupby(
    by='country',
    as_index=False
)[['recover_rate']].mean().round(2).nlargest(10, columns=['recover_rate'])


fig = px.bar(               # строим график
    data_frame=bar_data,    # датафрейм
    x="country",            # ось x
    y="recover_rate",       # ось y
    color='country',        # расцветка в зависимости от страны
    text = 'recover_rate',  # текст на столбцах
    orientation='v',        # ориентация графика
    height=500,             # высота
    width=1000,             # ширина
    title='Top 10 Countries for Recovery Rate' #заголовок
)


# График treemap() (древесная, или иерархическая, диаграмма)
"""
data_frame — DataFrame, по которому строится график;
path — категориальные признаки (их может быть несколько), в разрезе которых строится диаграмма;
values — показатель, по которому рассчитываются размеры прямоугольников.
"""


# Построим иерархическую диаграмму для среднего ежедневного показателя выздоровевших пациентов (daily_recovered) во всех странах
treemap_data = covid_df.groupby(        #считаем среднее ежедневно фиксируемое количество выздоровевших по странам
    by='country',
    as_index=False
)[['daily_recovered']].mean()


fig = px.treemap(                               # строим график
    data_frame=treemap_data,                    # DataFrame
    path=['country'],                           # категориальный признак, для которого строится график
    values='daily_recovered',                   # параметр, который сравнивается
    height=500,                                 # высота
    width=1000,                                 # ширина
    title='Daily Recovered Cases by Country'    # заголовок
)


# АНИМАЦИЯ ГРАФИКОВ ВО ВРЕМЕНИ

# Тепловая картограмма - choropleth
"""
Основные параметры метода choropleth()
- data_frame — DataFrame, по которому строится график;
- locations — название столбца, из которого берутся локации (столбец со странами или регионами);
- locationmode — режим геопривязки; 
определяет, как будет производиться сопоставление данных с картой в Plotly (возможно сопоставление по названию страны, "country_name", или по её трёхзначному шифру, согласно международному стандарту ISO-3);
- range_color — диапазон изменения цвета;
- animation_frame — анимирующий признак, изменяя который, мы получаем визуализацию во времени;
- color_continuous_scale — цветовая палитра.
"""


# Построим фоновую картограмму, которая покажет распространение (confirmed) коронавируса в мире во времени.
# Предварительно для правильного отображения на анимационном бегунке даты в таблице covid_df необходимо перевести обратно в строковый тип данных.
choropleth_data = covid_df.sort_values(by='date')
choropleth_data['date'] = choropleth_data['date'].astype('string')   # Преобразуем даты в строковый формат

fig = px.choropleth(                    # Cтроим график
    data_frame=choropleth_data,         # DataFrame
    locations="country",                # Cтолбец с локациями
    locationmode = "country names",     # Режим сопоставления локаций с базой Plotly
    color="confirmed",                  # От чего зависит цвет
    animation_frame="date",             # Анимационный бегунок
    range_color=[0, 30e6],              # Диапазон цвета
    title='Global Spread of COVID-19',  # Заголовок
    width=800,                          # Ширина
    height=500,                         # Высота
    color_continuous_scale='Reds'       # Палитра цветов
)


# Постройте анимированную тепловую картограмму для числа поставленных вакцин во всём мире (total_vaccinations). 
# На полученной карте найдите, чему равно количество вакцинированных в Японии (Japan) на 24 марта 2021 года (2021-03-24)
fig = px.choropleth(
    data_frame=choropleth_data,         # DataFrame
    locations="country",                # столбец с локациями
    locationmode = "country names",     # режим сопоставления локаций с базой Plotly
    color="total_vaccinations",         # от чего зависит цвет
    hover_name="country",               # группирующая переменная
    animation_frame="date",             # анимационный бегунок
    color_continuous_scale='Reds',      # палитра цветов
    range_color=[0, 600e6]              # диапазон цвета
)
fig.show()


# ТРЁХМЕРНАЯ ВИЗУАЛИЗАЦИЯ
"""
Для построения такой диаграммы используем метод scatter_3d(). 
Добавим несколько параметров:

z — параметр по оси аппликат;
log_x — установка логарифмического масштаба по оси x;
log_y — установка логарифмического масштаба по оси y.
"""


countries=['United States', 'Russia', 'United Kingdom', 'Brazil', 'France'] # Чтобы не перегрузить график, будем строить зависимость только в нескольких странах:
scatter_data = covid_df[covid_df['country'].isin(countries)]                # фильтруем таблицу по странам


fig = px.scatter_3d(            # Cтроим график
    data_frame=scatter_data,    # DataFrame
    x = 'daily_confirmed',      # ось абсцисс
    y = 'daily_deaths',         # ось ординат
    z = 'daily_vaccinations',   # ось аппликат
    color='country',            # расцветка в зависимости от страны
    log_x=True, 
    log_y=True,
    width=1000,
    height=700
)


# СОХРАНЕНИЕ ГРАФИКА PLOTLY
# Чтобы сохранить интерактивный график, построенный в библиотеке Plotly, используется метод фигуры fig.write_html('path/to/file.html')
#fig.write_html("data/scatter_3d.html")
