import pandas as pd

ufo_data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

# В данных есть следующие признаки:
# "City" — город, где был замечен НЛО;
# "Colors Reported" — цвет объекта;
# "Shape Reported" — форма объекта;
# "State" — обозначение штата;
# "Time" — время, когда был замечен НЛО (данные отсортированы от старых наблюдений к новым). 


# Прочитайте данные
print(ufo_data.head())


# Преобразование времени к формату datetime
ufo_data['Time'] = pd.to_datetime(ufo_data['Time'])

# Альтернативный вариант - результат тождественный 
ufo_data['Time'] = pd.to_datetime(ufo_data.Time)


# В каком году отмечается наибольшее количество случаев наблюдения НЛО в США?
# обратившись по атрибуту dt.year в столбце Time, мы можем «достать» год 
print('MAX number of UFO was seen in the USA in:', ufo_data['Time'].dt.year.mode()[0])


# средний интервал времени (в днях) между двумя последовательными случаями наблюдения НЛО в штате Невада (NV)
# метод diff() чтобы вычислить разницу между двумя соседними датами в столбце.
ufo_data['Date'] = ufo_data['Time'].dt.date                             # атрибут datetime date (dt.date) чтобы выделить дату из столбца Time.
print(ufo_data[ufo_data['State']=='NV']['Date'].diff().dt.days.mean())  # атрибут timedelta days (dt.days) чтобы перевести интервал времени в дни 