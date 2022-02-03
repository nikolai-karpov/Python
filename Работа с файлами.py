import os
from posixpath import split


# Для того чтобы начать работать с файлом, надо его открыть с помощью команды специальной функции open.

f = open('path/to/file', 'filemode', encoding='utf8')
# path/to/file — путь к файлу может быть относительным или абсолютным. Можно указывать в Unix-стиле (path/to/file) или в Windows-стиле (path\to\file).
"""filemode — режим, в котором файл нужно открывать.
Записывается в виде строки, может принимать следующие значения:
r — открыть на чтение (по умолчанию);
w — перезаписать и открыть на запись (если файла нет, то он создастся);
x — создать и открыть на запись (если уже есть — исключение);
a — открыть на дозапись (указатель будет поставлен в конец);
t — открыть в текстовом виде (по умолчанию);
b — открыть в бинарном виде.

encoding — указание, в какой кодировке файл записан (utf8, cp1251 и т. д.) 
По умолчанию стоит utf-8. 
При этом можно записывать кодировку как через дефис, так и без: utf-8 или utf8.
"""

"""
os.walk(top, topdown=True, onerror=None, followlinks=False)
 Параметры:
top - строка, вершинa каталога,
topdown=True - bool, направление обхода,
onerror=None - функция, которая сообщает об ошибке,
followlinks=False - bool, переходить ли по символическим ссылкам.
"""


# получить текущий путь

start_path = os.getcwd()
#print('отступ', end='\n')
#print('start_path:', start_path) 

os.chdir("..")                  # подняться на один уровень выше
start_path = os.getcwd()
#print('второй отступ', end='\n')
#print('start_path после os.chdir(".."):', start_path) 


os.chdir(start_path)            # Теперь вернемся в ту директорию, из которой стартовали
#print('os.chdir(start_path)', os.getcwd())

# получить весь список файлов, находящихся в директории
os.listdir()
#print(os.listdir())

#if 'tmp.py' not in os.listdir():
#    print("Файл отсутствует в данной директории")
    
    
# Для того чтобы склеивать пути с учётом особенностей ОС, следует использовать функцию
#print(start_path)
#print(os.path.join(start_path, 'test'))

def walk_desc(path=None):
    """Функция принимает от пользователя путь и выводит всю информацию о содержимом этой папки

    Args:
        path ([Путь], optional): [Если путь не указан, то сравнение начинается с текущей директории]. Defaults to None.
    """
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print("Текущая директория", root)
        print("---")

        if dirs:
            print("Список папок", dirs)
        else:
            print("Папок нет")
        print("---")

        if files:
            print("Список файлов", files)
        else:
            print("Файлов нет")
        print("---")

        if files and dirs:
            print("Все пути:")
        for f in files:
            print("Файл ", os.path.join(root, f))
        for d in dirs:
            print("Папка ", os.path.join(root, d))
        print("===")

walk_desc()


# ЧТЕНИЕ И ЗАПИСЬ ПОСТРОЧНО
"""для этого есть отдельные методы:
writelines — записывает список строк в файл;
f.writelines(sequence) - берет строки из sequence и записывает в файл f (без переносов)

readline — считывает из файла одну строку и возвращает её; возвращает строку (символы от текущей позиции до символа переноса строки):
readlines — считывает из файла все строки в список и возвращает их.

Метод f.writelines(<список строк>) не будет сам за вас дописывать символ конца строки ('\n'), 
поэтому при необходимости его нужно прописать вручную.
<список строк> = ["other string\n", "123\n", "test test\n"]
"""

f = open('test.txt', 'r', encoding='utf8')
print(f.readlines()) # считывает все строки в список и возвращает список
f.close()


# ФАЙЛ КАК ИТЕРАТОР
# Объект файл является итератором, поэтому его можно использовать в цикле for.

f = open('test.txt')  # можно перечислять строки в файле
for line in f:
    print(line, end='')

f.close()


# МЕНЕДЖЕР КОНТЕКСТА WITH
# Для явного указания места работы с файлом, а также чтобы не забывать закрывать файл после обработки, существует менеджер контекста with.

# В блоке менеджера контекста открытый файл «жив» и с ним можно работать, 
# при выходе из блока - файл закрывается.
with open("test.txt", 'rb') as f:
    a = f.read(10)
    b = f.read(23)

 
# Создайте любой файл на операционной системе под название input.txt
input_file = open('input.txt', 'r', encoding='utf8')

# построчно перепишите его в файл output.txt
output_file = open('output.txt', 'w', encoding='utf8')

for line in input_file:
    output_file.write(line)

f.close()

# Алтетрнативное решение
with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for line in input_file:
            output_file.write(line)
            
            
# Дан файл numbers.txt, компоненты которого являются действительными числами
filename = '/Volumes/HDD/Dropbox/Data Science/VS CODE/sf_data_science/homework/ООП/number.txt'
output = '/Volumes/HDD/Dropbox/Data Science/VS CODE/sf_data_science/homework/ООП/output.txt'

with open(filename, 'r') as number_file:
    with open(output, 'w') as output_file:
        min_number = max_number = float(number_file.readline())
        for line in number_file:
            if float(line) < min_number:
                 min_number = float(line)
            if float(line) > max_number:
                max_number = float(line)
        sum_ = min_number + max_number
        output_file.write(str(sum_))
        output_file.write('\n')

print('min_number', min_number)
print('max_number', max_number)
print('sum_', sum_) 

# Альтернатива


with open(filename) as f:
    min_ = max_ = float(f.readline())  # считали первое число
    for line in f:
        num =  float(line)
        if num > max_:
            max_ = num
        elif num < min_:
            min_ = num

    sum_ = min_ + max_

print('min_', min_)
print('max_', max_)
print('sum_', sum_)

with open(output, 'w') as f:
    f.write(str(sum_))
    f.write('\n')
    
  
# В текстовый файл fam_marks.txt построчно записаны фамилии и имена учащихся класса и их оценки за контрольную  
# Подсчитайте количество учащихся, count_p
# чья оценка меньше 3 баллов
filename = '/Volumes/HDD/Dropbox/Data Science/VS CODE/sf_data_science/homework/ООП/fam_marks.txt'
count_p = 0
with open(filename) as f:
    for line in f:
        str_ =  line.split()
        for el in str_:
            if el.isdigit():
                if int(el) < 3:
                    count_p += 1
print(count_p) 

# Короткое решение
count = 0
for line in open(filename):
    points = int(line.split()[-1])
    if points < 3:
        count += 1
        
        
# Выполните реверсирование строк файла (перестановку строк файла в обратном порядке).

filename = '/Volumes/HDD/Dropbox/Data Science/VS CODE/sf_data_science/homework/ООП/fam_marks.txt'
output = '/Volumes/HDD/Dropbox/Data Science/VS CODE/sf_data_science/homework/ООП/output.txt'

with open(filename, 'r') as input_file:
    with open(output, 'w') as output_file:
        for line in reversed(input_file.readlines()):
            output_file.write(line)
