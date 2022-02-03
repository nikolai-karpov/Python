import pandas as pd


citibike_tripdata = pd.read_csv('data/citibike-tripdata.csv', sep=',')

# Датасет представляет собой таблицу с информацией о 300 тысячах поездок за первые пять дней сентября 2018 года и включает в себя следующую информацию:

# starttime — время начала поездки (дата, время);
# stoptime — время окончания поездки (дата, время);
# start station id — идентификатор стартовой стоянки;
# start station name — название стартовой стоянки;
# start station latitude, start station longitude — географическая широта и долгота стартовой стоянки;
# end station id — идентификатор конечной стоянки;
# end station name — название конечной стоянки;
# end station latitude, end station longitude — географическая широта и долгота конечной стоянки;
# bikeid — идентификатор велосипеда;
# usertype — тип пользователя (Customer — клиент с подпиской на 24 часа или на три дня, Subscriber — подписчик с годовой арендой велосипеда);
# birth year — год рождения клиента;
# gender — пол клиента (0 — неизвестный, 1 — мужчина, 2 — женщина).


# Сколько пропусков в столбце start station id?
print(citibike_tripdata.info())
print(300000-299831)


# Какой тип данных имеют столбцы starttime и stoptime?
print(citibike_tripdata['starttime'].dtypes)
print(citibike_tripdata['starttime'].dtypes)


# Найдите идентификатор самой популярной стартовой стоянки start station id . 
# Запишите идентификатор в виде целого числа.
print(citibike_tripdata['start station id'].mode()[0])


# Велосипед с каким идентификатором bikeid является самым популярным?
print(citibike_tripdata['bikeid'].info())


# Какой тип клиентов (столбец usertype) является преобладающим — Subscriber или Customer? 
# В качестве ответа запишите долю клиентов преобладающего типа среди общего количества клиентов. 
# Ответ округлите до сотых.
mode_usertype = citibike_tripdata['usertype'].mode()[0]                                                 # Записываем самый популярный тип клиента в переменную

print('Преобладающим типом клиентов является: ', mode_usertype)
print('Кол-во уникальных клиентов по типам: ', citibike_tripdata['usertype'].value_counts())
print('Доля клиентов в %: ', round(citibike_tripdata['usertype'].value_counts(normalize=True), 2)*100)  # normalize=True, возвращаемый объект будет содержать относительные частоты уникальных значений.

count_mode_user = citibike_tripdata[citibike_tripdata['usertype'] == mode_usertype].shape[0]            # Записываем самый популярный тип клиента в переменную, с помощью атрибута shape[0], возвращаем только количество строк
print('Преобладающая доля: ',round(count_mode_user / citibike_tripdata.shape[0], 2))


# Кто больше занимается велоспортом — мужчины или женщины? 
print(citibike_tripdata['gender'].mode()[0])

# Альтернативный вариант
male_count = citibike_tripdata[citibike_tripdata['gender'] == 1].shape[0]
female_count = citibike_tripdata[citibike_tripdata['gender'] == 0].shape[0]
print(max([male_count, female_count]))

# Число поездок мужчин gender 1 — мужчина.
print('Число поездок мужчин: ', citibike_tripdata[citibike_tripdata['gender'] == 1].shape[0])

# Число поездок женщин gender 2 — женщина.
print('Число поездок женщин: ', citibike_tripdata[citibike_tripdata['gender'] == 2].shape[0])


# Число стартовых start station name 
print('Число стартовых стоянок: ', citibike_tripdata['start station name'].nunique())

# Число конечных стоянок end station name?
print('Число конечных стоянок: ', citibike_tripdata['end station name'].nunique())


# минимальный возраст клиента?  birth year — год рождения клиента
print(2018 - int(citibike_tripdata['birth year'].max()))


# Самой непопулярная стартовой стоянкой из тех, которыми воспользовались клиенты, является?
print('Стартовые площадки: ', citibike_tripdata['start station name'].value_counts(normalize=True)*100)
print('Минимальное значение для стартовой площадки: ', citibike_tripdata['start station name'].value_counts().min())
print(citibike_tripdata['start station name'].describe())


# Удалить столбцы с идентификатором и названием стартовой и конечной стоянки.  метод drop()
# Удалите признаки идентификаторов стоянок. start station id и end station id
# axis — ось совершения операции, axis=0 — удаляются строки, axis=1 — удаляются столбцы;
citibike_tripdata = citibike_tripdata.drop(['start station id', 'end station id'], axis=1)

# Альтернативный вариант:
#citibike_tripdata.drop(['start station id','end station id'],axis=1,inplace=True)

# Сколько столбцов осталось?
#print(citibike_tripdata.info())


# Замените признак birth year на более понятный признак возраста клиента age. 
# Годом отсчёта возраста выберите 2018 год.
citibike_tripdata['Age'] = 2018 - citibike_tripdata['birth year']

# Столбец birth year удалите из таблицы. 
citibike_tripdata.drop(['birth year'], axis=1, inplace=True)

# Сколько поездок совершено клиентами старше 60 лет?
print(citibike_tripdata[citibike_tripdata['Age'] > 60].shape[0])


# Создайте признак длительности поездки trip duration. 
# Для этого вычислите интервал времени между временем окончания поездки (stoptime) и временем её начала (starttime) в секундах. 
citibike_tripdata['starttime'] = pd.to_datetime(citibike_tripdata['starttime'])
citibike_tripdata['stoptime'] = pd.to_datetime(citibike_tripdata['stoptime'])

citibike_tripdata['trip duration'] = (citibike_tripdata['stoptime'] - citibike_tripdata['starttime']).dt.seconds

# В качестве ответа запишите среднюю длительность поездки в секундах. 
# Ответ округлите до целого.
print(round(citibike_tripdata['trip duration'].mean()))


# Подсчет гонок в выходные
citibike_tripdata['WeekdayStart'] = citibike_tripdata['starttime'].dt.dayofweek  # номер дня недели, где 0 — понедельник, 6 — воскресенье
# citibike_tripdata['WeekdayStart']  день недели в который стартовала гонка

# Выясните, сколько поездок начиналось в выходные.
weekend_count = citibike_tripdata[(citibike_tripdata['WeekdayStart'] == 5) | (citibike_tripdata['WeekdayStart'] == 6)].shape[0] # сколько стартов в субботу и воскресенье
print('В выходные стартавало', weekend_count, 'поездок')

# Альтернативное решение по заданию
# Создайте «признак-мигалку» weekend, который равен 1, если поездка начиналась в выходной день (суббота или воскресенье)
# и 0 — в противном случае. 
citibike_tripdata['weekend'] = citibike_tripdata['WeekdayStart'].apply(lambda x: 1 if x > 4 else 0)
weekend_count = citibike_tripdata[(citibike_tripdata['weekend'] == 1)].shape[0] # сколько стартов в субботу и воскресенье
print('В выходные стартавало', weekend_count, 'поездок')

# Идеальное решение подсказка
# weekday = citibike_tripdata['starttime'].dt.dayofweek
# citibike_tripdata['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
# print(citibike_tripdata['weekend'].sum())


# ВЫДЕЛЕНИЕ АТРИБУТОВ DATETIME
# Тип данных datetime позволяет с помощью специального аксессора dt выделять составляющие времени из каждого элемента столбца, такие как:
# time — время;
# hour, minute, second — час, минута, секунда;


# Создайте признак времени суток поездки time_of_day. 
# Время суток будем определять из часа начала поездки. 
# Условимся, что:
# поездка совершается ночью (night), если её час приходится на интервал от 0 (включительно) до 6 (включительно) часов;
# поездка совершается утром (morning), если её час приходится на интервал от 6 (не включительно) до 12 (включительно) часов;
# поездка совершается днём (day), если её час приходится на интервал от 12 (не включительно) до 18 (включительно) часов;
# поездка совершается вечером (evening), если её час приходится на интервал от 18 (не включительно) до 23 часов (включительно).

def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'
    
    
citibike_tripdata['time_of_day'] = citibike_tripdata['starttime'].dt.hour.apply(get_time_of_day)

a = citibike_tripdata[citibike_tripdata['time_of_day'] == 'day'].shape[0]
b = citibike_tripdata[citibike_tripdata['time_of_day'] == 'night'].shape[0]

# Во сколько раз количество поездок, совершённых днём, больше, чем количество поездок, совёршенных ночью, за представленный в данных период времени? 
# Ответ округлите до целых.
print(round(a / b))



