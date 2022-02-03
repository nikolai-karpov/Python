import pandas as pd

orders_df = pd.read_csv('data/orders.csv', sep=';')
print(orders_df)

product_df = pd.read_csv('data/products.csv', sep=';')
print(product_df)

# Объедините заданные таблицы в таблицу orders_products, 
# чтобы в результирующей таблице оказалась информация обо всех заказах, 
# но не оказалось информации о продуктах, на которых заказов ещё не поступало. 
orders_products = orders_df.merge(
    product_df, 
    left_on='ID товара',
    right_on='Product_ID',
    how='left')

print(orders_products)


# Какой идентификатор (Order ID) из orders.csv имеет заказ, для которого не оказалось информации о товаре products.csv?
res = orders_products[orders_products['Product_ID'].isnull() == True]['Order ID']
print(res)


# На какой товар была произведена отмена? вывестие его Name
res = orders_products[orders_products['Статус'] == 'Отменён']['Name']
print(res)


# Какой покупатель принёс наибольшую суммарную прибыль интернет-магазину за указанный период? 
# вывести ID Покупателя
orders_products['Profit'] = orders_products['Price'] * orders_products['Количество']
profit = orders_products[orders_products['Оплачен'] == 'Да'].groupby('ID Покупателя')['Profit'].sum().sort_values(ascending=False)
print(profit)

