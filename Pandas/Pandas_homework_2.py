import pandas as pd


students_performance = pd.read_csv('data/students_performance.csv', sep=',')
# gender — пол;
# race/ethnicity — раса/этническая принадлежность;
# parental level of education — уровень образования родителей;
# lunch — какие обеды получал студент во время обучения (standard — платный, free/reduced — бесплатный);
# test preparation course — посещал ли студент курсы подготовки к экзаменам (none — не посещал, completed — посещал);
# math score, reading score, writing score — баллы по математике, чтению и письму по сто балльной шкале.


# Данные о скольких студентах содержатся в таблице?
print(students_performance.shape[0])


# Каков балл по письму writing score у студента под индексом 155?
print(students_performance.loc[155, 'writing score'])


# Сколько суммарно пропущенных значений в таблице? ответ ноль
print(students_performance.info())


# Сколько столбцов в таблице имеет тип данных object?
print(students_performance.describe(percentiles=None, include=object, exclude=None, datetime_is_numeric=False))


# Каков у студентов средний балл по математике? math score
# int(student_data['math score'].mean())
print(students_performance['math score'].mean())


# Какая расовая группа race является самой крупной в учебном заведении?
print(students_performance['race/ethnicity'].mode())
print(students_performance['race/ethnicity'].value_counts())


# Каков средний балл по чтению reading score у студентов, которые посещали курсы подготовки к экзаменам?
print(round(students_performance[students_performance['test preparation course'] == 'completed']['reading score'].mean()))


# Сколько студентов получили 0 баллов по математике?
print(students_performance[students_performance['math score'] == 0].shape[0])
 
 
# Проверьте гипотезу: 
# у студентов с оплачиваемым питанием средний балл по математике выше, чем у студентов с льготным питанием.
# В качестве ответа напишите наибольший средний балл по математике среди этих групп студентов.
print(int(students_performance[students_performance['lunch'] == 'standard']['math score'].mean()))
print(int(students_performance[students_performance['lunch'] == 'free/reduced']['math score'].mean()))


# Каков процент студентов, родители которых имеют высшее образование 
# parental level of education уровня бакалавриата (bachelor's degree)?
print(round((students_performance['parental level of education'].value_counts(normalize=True))*100))


# Насколько медианный балл по письму writing score у студентов в расовой группе А 
# отличается от среднего балла по письму у студентов в расовой группе C?
group_a_median = students_performance[students_performance['race/ethnicity'] == 'group A']['writing score'].median() 
group_c_mean =  students_performance[students_performance['race/ethnicity'] == 'group C']['writing score'].mean()
print('насколько медианный балл по письму группе А отличается отсреднего балла группе C', abs(round(group_a_median - group_c_mean)))
