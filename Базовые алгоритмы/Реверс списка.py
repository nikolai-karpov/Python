my_list = [1]


for i in range(10):
    my_list.append(my_list[i] * 2)
    print(my_list)
    
    
my_list.sort(reverse = True) # реверс для списка

print('end of cycle', my_list)