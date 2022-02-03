# переведем даты из строкового формата в datetime
df['col'] = pd.to_datetime(df['col'])

df['col'] = df['col'].astype('Int64')

# Оптимизируем занимаемую память (уменьшаем занимаемую память в два раза)
df['col'] = df['col'].astype(np.int8)


# Выделяем категориальные признаки
df['col'] = df['col'].astype('category')
