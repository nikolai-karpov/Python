graph = {}

# Необходимо сохранять соседей и стоимость перехода
graph['start'] = {}         # хеш-таблица для получения всех соседей начального узла
graph['start']['a'] = 6     # Стоиомсть перехода к узлу А
graph['start']['b'] = 2     # Стоиомсть перехода к узлу B

# print(graph['start'].keys())
# ['a', 'b']

# Чтобы узнать вес ребер
# print('Вес ребра A:', graph['start']['a'])
# 2
# print('Вес ребра B:', graph['start']['b'])
# 6


# Включим в граф остальные узлы соседей
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}                       # У конечного узла нет соседей


# Хеш-таблица для хранения стоимости всех узлов
infinity = float('inf')                 # Если стоимость еще не известна, она считается безконечной
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity


# Хеш-таблица для хранения родителей
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None


processed = []                          # Массив для отслеживания всех отработанных узлов


# Поиск узла с наименьшей стоимостью
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    
    for node in costs:                                      # перебрать все узлы
        cost = costs[node]
        
        if cost < lowest_cost and node not in processed:    # Если это узел с наименьшей стоимостью из уже виденных и он еще не был обработан
            lowest_cost = cost                              # он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    
    return lowest_cost_node


node = find_lowest_cost_node(costs)      # Найти узел с наименьшей стоимостью среди необработанных

while node is not None:                  # Цикл завершится после обработки всех узлов
    cost = costs[node]                   # Получить стоимсоть узла
    neighbors = graph[node]              # Получить соседей узла
    
    for n in neighbors.keys():           # Перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n]  
        
        if costs[n] > new_cost:          # Если к соседу можно быстрее добраться через текущий узел
            costs[n] = new_cost          # Обновить стоимость для этого узла
            parents[n] = node            # Этот узел становится новым родителем для соседа
        
            
    processed.append(node)               # Узел отмечается как отработанный
    node = find_lowest_cost_node(costs)  # Найти следующий узел для обработки и повторить цикл
    

print('Кротчайший путь', new_cost, 'через', parents[n])
