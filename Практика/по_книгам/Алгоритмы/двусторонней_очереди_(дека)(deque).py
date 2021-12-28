graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = [] 
from collections import deque 
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [] # Этот массив используется дпя отслеживания уже проверенных людей
    while search_queue:
        person = search_queue.popleft()
        if not person in searched: # Человек проверяется только в том спучае, еспи он не проверялся ранее
            if person=="alice": # person_is_seller(person)
                print (person +" is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person) # Человек помечается как уже проверенный
    return False
search("you")