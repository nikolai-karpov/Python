# Напишите декоратор, который запрашивает имя пользователя и проверяет, есть ли оно в списке пользователей.
# Если да, то мы можем выполнить следующую нашу функцию:


from functools import cache


users_list = ['admin', 'ivan', 'ivan_ivan']

def user_auth(func):
    def wrapper():
        user = input("Enter username: ")
        if user in users_list:
            print("User authed")
            func()
        else:
            print("Unknown user!")      # Если пользователя нет в списке, нужно вывести об этом сообщение
                                        # и пропустить выполнение функции get_data_from_database().
            
    return wrapper                      # Возвращаем результат выполнения функции


@user_auth                              # Перед начал исполнения данной функции запустится декоратор
def get_data_from_database():
    print("Super secure data from database")



get_data_from_database()


# Проверка избирателей
voted = {}
def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')
        
        
# Работа с кеш
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]   # Возвращаются кешированные данные
    else:
        data = get_data_from_server(url)
        cache[url] = data   # данные сначала сохраняются в кеш
        return data