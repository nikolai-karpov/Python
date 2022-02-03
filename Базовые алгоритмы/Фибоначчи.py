# Вычисление числа Фибоначчи:
    def fibb(n):
 if n == 0:
 return 0  elif n == 1:
 return 1  elif n == 2:
 return 1  else:
 return fibb(n-1) + fibb(n-2)
 print(fibb(10)) 
# 55