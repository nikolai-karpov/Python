def is_palindrom():
    word = input('Введите слово')
    word = word.lower()
    return word == word[::-1]
   

is_palindrom()

is_palindrom = lambda string: 'yes' if string.lower() == string[::-1].lower() else 'no' 
is_palindrom('Радар')