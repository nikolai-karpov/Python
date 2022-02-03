import numpy as np
 
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])

# сумма длин сонаправленных векторов должна быть равной длине суммы двух векторов
# найдите пару сонаправленных векторов
len_a = np.linalg.norm(a)
len_b = np.linalg.norm(b)
len_c = np.linalg.norm(c)


len_a_b = np.linalg.norm(a + b) # Сумма длин двух векторов
len_b_c = np.linalg.norm(b + c)
len_a_c = np.linalg.norm(a + c)


print('The length of the vector a', len_a) # Длина вектора
print('The length of the vector b', len_b)
print('The length of the vector c', len_c)


np.dot(a, b)     # равенство скалярного произведения нулю означает перпендикулярность рассматриваемых векторов
np.dot(a, c)
np.dot(b, c)

print('The sum of the lengths of vectors a and b', len_a_b)
print('Checking their equality', len_a_b == len_a + len_b)
# False

print('The sum of the lengths of vectors b and c', len_b_c)
print('Checking their equality', len_b_c == len_b + len_c)
# False

print('The sum of the lengths of vectors a and c', len_a_c)
print('Checking their equality', len_a_c == len_a + len_c)
# True


# Найдите пару векторов, расстояние между которыми больше 100.

len_a_b = np.linalg.norm(a - b)
len_b_c = np.linalg.norm(b - c)
len_a_c = np.linalg.norm(a - c)
 
print(len_a_b)
# 86.2902080192185
print(len_b_c)
# 121.19405926034493
print(len_a_c)
# 49.13247398615299


# Найдите пару перпендикулярных векторов с помощью скалярного произведения (оно должно быть равно нулю).
dot_a_b = np.dot(a, b)
dot_b_c = np.dot(b, c)
dot_a_c = np.dot(a, c)
 
print(dot_a_b)
# 34
print(dot_b_c)
# 68
print(dot_a_c)
# 4828