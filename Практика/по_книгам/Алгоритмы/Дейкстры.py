# Сначала необходимо реализовать граф. Как и в главе 6, для этого будет использована хеш-таблица: 
graph={}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print (graph["start"].keys())
print (graph["start"]["a"])
print (graph["start"]["b"])
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {} # У конечного уэла нет соседей
# Код создания таблицы стоимостей costs:
infinity = float("inf") # бесконечность
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity 
# Для родителей также создается отдельная таблица:
# Код создания хеш-таблицы родителей:
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None 
processed = [] # массив для отслеживания всех уже обработанных узлов
# С функцией find_lowest_cost_node узел с наименьшей стоимостью находится проще простого.
# Код выглядит так: 
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Перебрать все узлы
        cost = costs[node]
        # Если это узел с наименьшей стоимостью
        # из уже виденных и он еще не был обработан...
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost # он назначается новым узлом
            # с наименьшей стоимостью 
            lowest_cost_node = node
    return lowest_cost_node # узлом с наименьшей стоимостью
    
# Так выглядит алгоритм Дейкстры на языке Pythoв!
# Найти узел с наименьшей стоимостью среди необработанных
node = find_lowest_cost_node(costs)
# Если обработаны все узлы, цикл while завершен
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Перебрать всех соседей текущего узла 
        new_cost = cost + neighbors[n]
        # Если к соседу можно быстрее добраться через текущий узел ...
        if costs [n] > new_cost:
            costs [n] = new_cost # ... обновить стоимость для этого узла
            parents [n] = node # Этот узел становится новым родителем для соседа 
    processed.append (node) # Узел помечается как обработанный
    node = find_lowest_cost_node(costs) # Найти следующий узел для обработки и повторить цикл  