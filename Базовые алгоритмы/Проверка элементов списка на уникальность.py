# Проверьте, все ли элементы в списке являются уникальными.
# Используйте возможности set.
# len(s) - число элементов в множестве (размер множества).


list_ = [-5, 2, 4, 8, 12, -7, 5]

a = len(list_)
b = len(set(list_))
if a == b:
    print('all elements are unique')