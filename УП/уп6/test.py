# множество - специальный контейнер, который хранит в себе не повторяющиеся значения в произвольном порядке
a = set('hello')
print(a)
# frozenset отличие заключается в том что set можно изменить, а в frozenset тип не изменяем
b = frozenset('hello')
