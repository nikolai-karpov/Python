deposit = 1000          # Олег положил тысячу рублей в банк под 8% годовых
year = 0
                        # Через сколько лет у него на счету будет не менее трёх тысяч рублей?
while deposit < 3000:
    deposit += deposit*0.08
    year += 1

print (year, deposit)