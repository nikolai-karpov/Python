sqrt = lambda x: x**0.5
print(sqrt(25))

myList_1 = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x*2, myList_1))) # Благодрая map с каждым элементом myList_1 будет проведена x*2

myList_2 = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: x>3, myList_2))) # Отфильтрует из myList_2 те элементы, которые соответствуют x>3 

myList_3 = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x**2 if x==2
                               else x**3
                                 if x==4
                                   else x, myList_3)))

def convert(num):
    if num==2:
        n_str = num**2
    elif num==4:
        n_str = num**3
    else:
        n_str = num
    return n_str

myList_4 = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: convert(x), myList_4))) # К каждому элементу myList_4 применится функция convert
print(list(map(convert, myList_4)))


# melb_df['StreetType'] = melb_df['StreetType'].apply(lambda x: 'Av' if x == 'Avenue')

myList_5 = ['av', 'Av', 'ave']
print(list(map(lambda x: 'ave' if x=='av'
                               else 'ave'
                                 if x=='Av'
                                   else x, myList_5)))








