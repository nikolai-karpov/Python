import pandas as pd
"""
Ваша задача очистить данную таблицу от пропусков следующим образом:
- Если признак имеет больше 50% пропущенных значений - удалите его
- Для оставшихся данных: если в строке более 2 пропусков - удалите строку
- Для оставшихся данных: числовые признаки заполните средним значением, а категориальные - модой
Результат должен находиться в переменной df
"""
df = pd.read_csv('./Root/data/test_data.csv')

# Отбрасываем столбцы с числом пропусков более 50%
n_rows = df.shape[0]   # число строк в таблице
df = df.dropna(thresh=n_rows*0.5, axis=1)

# Отбрасываем строки с числом пропусков более 2 в строке
n_columns = df.shape[1] # число признаков после удаления столбцов
df = df.dropna(how='any', thresh=n_columns-2, axis=0)

#создаем словарь имя столбца: число(признак) на который надо заменить пропуски
values = {
    'one': df['one'].mean(),
    'two': df['two'].mean(),
    'three': df['three'].mean(),
    'four': df['four'].mode()[0]
}

#заполняем пропуски в соответствии с заявленным словарем
df = df.fillna(values)

print(df)
