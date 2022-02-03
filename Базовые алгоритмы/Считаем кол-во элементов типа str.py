# С помощью цикла for посчитайте количество элементов типа str в списке


my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 2.5, [1, 2], 'another']

a = 0                               #Создаем счетчик


for form in my_list:
    if type(form) is str:
        a = a + 1                   #Засчитываем совпадение типа
print('Total str is: ', a)