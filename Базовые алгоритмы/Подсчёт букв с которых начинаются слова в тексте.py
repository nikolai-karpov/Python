# Напишите функцию, которая принимает на вход строку и подсчитывает в ней количество слов начинающихся на каждую букву алфавита.
# Возвращать функция должна словарь следующего вида:
# {'a': 10, 'b': 3, 'c': 0, ...}
# Для задания словаря используйте строку с алфавитом:
# alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
# Словарь с буквами создайте с помощью генератора.
# Не забудьте, что слова в предложении могут начинаться с большой буквы!


def count_words(sentence_str):
    alphabet_str = "abcdefghijklmnopqrstuvwqyz"
    letters_dict = {letter: 0 for letter in alphabet_str}

    words_list = sentence_str.lower().split()
    for word in words_list:
        letters_dict[word[0]] += 1
    return letters_dict

str_example = "Fibonacci numbers are strongly related to the golden ratio: Binet's formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two consecutive Fibonacci numbers tends to the golden ratio as n increases."
print(count_words(str_example))
