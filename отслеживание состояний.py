class DepartmentReport():
    def __init__(self, company_name):  
        self.revenues = []  
        self.company_name = company_name  
              
    def add_revenue(self, amount):
        self.revenues.append(amount)
 
    def average_revenue(self):
        average_revenue = (int(sum(self.revenues)/len(self.revenues)))
        return(f'Average department revenue for {self.company_name}: {average_revenue}')

       
report = DepartmentReport("Danon")
report.add_revenue(1_000_000)
report.add_revenue(400_000)

print(report.average_revenue())
# => Average department revenue for Danon: 700000


# ОТСЛЕЖИВАНИЕ СОСТОЯНИЯ

class Client():  
    # Базовые данные  
    def __init__(self, email, order_num, registration_year):  
        self.email = email  
        self.order_num = order_num  
        self.registration_year = registration_year  
        self.discount = 0  
          
    # Оформление заказа  
    def make_order(self, price):  
        self.update_discount()  
        self.order_num += 1  
        # Здесь было бы оформление заказа, но мы просто выведем его цену  
        discounted_price = price * (1 - self.discount)   
        print(f"Order price for {self.email} is {discounted_price}")  
              
    # Назначение скидки  
    def update_discount(self):   
        if self.registration_year < 2018 and self.order_num >= 5:  
            self.discount = 0.1   
              
  
# Применение  
          
# Сделаем подобие базы  
client_db = [   
    Client("max@gmail.com", 2, 2019),  
    Client("lova@yandex.ru", 10, 2015),  
    Client("german@sberbank.ru", 4, 2017)  
]  
  
  
# Сгенерируем заказы  
client_db[0].make_order(100)  
# => Order price for max@gmail.com is 100  
  
client_db[1].make_order(200)  
# => Order price for lova@yandex.ru is 180.0  
  
client_db[2].make_order(500)  
# => Order price for german@sberbank.ru is 500  
  
client_db[2].make_order(500)  
# => Order price for german@sberbank.ru is 450.0


class User():
    def __init__(self, email, password, balance):
        self.email = email
        self.password = password
        self.balance = balance
        update_balance=0

    def login(self, email, password):
        if self.email==email and self.password==password:
            answer=True
        else:
            answer=False
        return answer
        
    def update_balance(self, amount):
        self.balance += amount
        return self.balance
    
        
user = User("gosha@roskino.org", "qwerty", 20_000)
user.login("gosha@roskino.org", "qwerty123")
# => False
user.login("gosha@roskino.org", "qwerty")
# => True
user.update_balance(200)
user.update_balance(-500)
print(user.balance)
# => 19700
