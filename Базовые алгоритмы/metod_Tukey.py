import pandas as pd

def outliers_iqr_mod(data, feature, left=1.5, right=1.5):
    """
    параметры left и right, задают число IQR влево и вправо от границ ящика (по умолчанию они равны 1.5).
    Функция  возвращает потенциальные выбросы и очищенный DataFrame.
    """
    x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x<lower_bound) | (x > upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned


outliers, cleaned = outliers_iqr(sber_data, 'full_sq')

print(f'Число выбросов по методу Тьюки: {outliers.shape[0]}')

print(f'Результирующее число записей: {cleaned.shape[0]}')