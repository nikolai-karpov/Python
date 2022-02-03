def get_avg_hw_grade(students, exp=None):
    sum_hw = 0
    counter = 0
    for student in students:
        if student['program_exp'] == exp or exp is None:
            sum_hw += sum(student['grade']) / len(student['grade'])
            counter += 1
    return round(sum_hw / counter, 2)

print(get_avg_hw_grade(students_list, False))
print(get_avg_hw_grade(students_list, True))
print(get_avg_hw_grade(students_list))


# Если нужно разделить по полу
def get_avg_hw_grade(students, exp=None, gender=None):
    sum_hw = 0
    counter = 0
    for student in students:
        if (student['program_exp'] == exp or exp is None) and \
           (student['gender'] == gender or gender is None):
            sum_hw += sum(student['grade']) / len(student['grade'])
            counter += 1
    return round(sum_hw / counter, 2)

print(get_avg_hw_grade(students_list))
print(get_avg_hw_grade(students_list, False))
print(get_avg_hw_grade(students_list, True))
print(get_avg_hw_grade(students_list, False, 'м'))
print(get_avg_hw_grade(students_list, True, 'ж'))

print(get_avg_hw_grade(students_list, None, 'ж'))
print(get_avg_hw_grade(students_list, gender='ж'))


# Выбор метрик от ввода
def main(students):
    while True:
        user_input = input('Введите команду')
        if user_input == '1':
            print(get_avg_ex_grade(students))
        elif user_input == '2':
            print(get_avg_hw_grade(students))
        elif user_input == '3':
            print(get_avg_hw_grade(students, True))
        elif user_input == 'q':
            print('Выход')
            break

main(students_list)
