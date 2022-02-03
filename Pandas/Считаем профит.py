"""
    Создайте функцию create_companyDF(income, expenses, years), которая  возвращает DataFrame, 
    составленный из входных данных со столбцами “Income” и “Expenses” 
    и индексами, соответствующим годам рассматриваемого периода.
    
    А также напишите функцию get_profit(df, year), которая возвращает разницу между доходом и расходом, 
    записанных в таблице df, за год year.
    Учтите, что если информация за запрашиваемый год не указана в вашей таблице вам необходимо вернуть None. 
    
"""
# Для проверки вхождения запрашиваемого года в перечень индексов таблицы вам поможет атрибут df.index, 
# который возвращает список индексов таблицы.

import pandas as pd

def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
        'income': income,
        'expenses': expenses,
        }, 
        index = years
    )
    return df

def get_profit(df, year):
    if year in df.index:
        profit = df.loc[year, 'income'] - df.loc[year, 'expenses']
    else:
        profit=None
    return profit

if __name__ == '__main__':
    expenses = [156, 130, 270]
    income = [478, 512, 196]
    years = [2018, 2019, 2020]
    
    scienceyou = create_companyDF(income, expenses, years)
    print(get_profit(scienceyou, 2020)) 
