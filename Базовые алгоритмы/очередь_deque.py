from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'              # Если заканчивается на m продавец найден


def search(name):
    search_queue = deque()              # Создание новой очереди
    search_queue += graph[name]         # Все соседи добавляются в очередь поиска
                                        # graph[name] возвращает список соседей you
    searched = []                       # Массив для отслеживания уже проверенных
    while search_queue:                 # Пока очередь не пуста
        person = search_queue.popleft() # из очереди извлекается первый человек
        if not person in searched:      # Проверяем только в том случае если он не проверялся ранее
            if person_is_seller(person):    # Проверяем является ли человек продавцем
                print(person + 'is seller') # действие, если условие совпало
                return True
            else:
                search_queue += graph[person]   # Если не является, все друзья этого человека добавляются в очередь списка
                searched.append(person)
                
    return False    # Есди выполнение дошло до этой строки, значит в очереди нет продавца


