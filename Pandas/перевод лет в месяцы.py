# Напишите функцию, аргументом которой является строка столбца с опытом работы.
# Функция должна возвращать опыт работы в месяцах
# Не забудьте привести результат к целому числу


import pandas as pd

def get_experience(arg):
    args_splited = arg.split(' ') 
    year_key_words = ['лет', 'год', 'года']
    month_key_words = ['месяца', 'месяцев', 'месяц']
    year = 0
    month = 0
    for i in range(len(args_splited)):
        if args_splited[i] in year_key_words:
            year =  args_splited[i-1]
        if args_splited[i] in month_key_words:
            month = args_splited[i-1]
    return int(year)*12 + int(month)
    
    
if __name__ == '__main__':
    experience_col = pd.Series([
        'Опыт работы 8 лет 3 месяца',
        'Опыт работы 3 года 5 месяцев',
        'Опыт работы 1 год 9 месяцев',
        'Опыт работы 3 месяца',
        'Опыт работы 6 лет'
        ])
    experience_month = experience_col.apply(get_experience)
