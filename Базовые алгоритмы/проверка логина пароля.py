username = input('username: ')
password = input('password: ')
user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}


def check_user(username, password):
    if username in user_database:
        if password in user_database[username]:
            return True
        else:
            return False
    else:
            return False
            
            
print(check_user(username, password))