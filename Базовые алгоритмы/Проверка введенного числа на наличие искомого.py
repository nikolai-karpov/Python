# Дано двузначное число. 
# Определите, входит ли в него цифра 5. 


a = input('enter a two-digit number: ')
while not a.isdigit():
    a = input('enter a two-digit number: ')
try:
    a = int(input('enter a two-digit number: '))
except ValueError:
        print("Sorry is not a valid input")
        a = int(input('enter a two-digit number: '))
while -10 > a < 10:        # Loop until it is a blank line
    a = int(input('enter a two-digit number: '))
if '5' in str(a):
    print('there is 5')
else:
    print('there is not 5')
    
#второй вариант решения задачи  

a = int(input('enter a two-digit number: '))
while -9 < a < 10:        # Loop until it is a blank line
    a = int(input('enter a two-digit number: '))
if 5 in map(int, str(a)):  
    print('there is 5')
else:
    print('there is not 5')
    
#Попробуйте решить задачу с использованием целочисленного деления и деления с остатком.
n = 15
first_digit = n // 10
second_digit = n % 10

print((first_digit == 5) or (second_digit == 5))

#Мой вариант
try:
    a = int(input('enter a two-digit number: '))
except ValueError:
        print("Sorry is not a valid input")
        a = int(input('enter a two-digit number: '))
first_digit = a // 10
second_digit = a % 10
if first_digit == 5 or second_digit == 5:
    print('There is 5')
elif first_digit != 5 and second_digit != 5:
    print('There is not 5')