# если мы положим Dumper в файл dumper.py в корне проекта, то его можно импортировать командой:
# from dumper import Dumper 
# Пишем from <имя файла без .py> import <имя класса>
# Например
    """папка helpers в ней файлы:
-- __init__.py
-- dumper.py
-- data_frame.py
-- client.py
    """
    
from helpers.dumper import Dumper           # импортируем класс Dumper из файла dumper в папке helpers
from helpers.data_frame import DataFrame    # импортируем класс DataFrame из файла data_frame в папке helpers
from helpers.client import Client           # импортируем класс Client из файла client в папке helpers