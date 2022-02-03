district_1 = {'flat_1': 10500, 'flat_2': 11000}
district_2 = {'flat_3': 15000}
district_3 = {'flat_4': 6500, 'flat_5': 7000, 'flat_6': 6000}  

def mean_price(*args): 
    price = 0 
    count = 0 
    for i in args: 
        price += sum(i.values())
        count += len(i.values())
    return price / count
mean_price(district_2, district_1)