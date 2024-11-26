immutable_var = (1, 2, 'string', True, [1, 2, 3])
print(immutable_var)
#immutable_var [0] = 4 #Кортеж - это неизменяемый тип данных для хранения упорядоченной последовательности элементов. В кортеже нельзя заменить значение элемента, добавить или удалить элемент.  'tuple' object does not support item assignment
mutable_list = ([1, 2, 3, 'string', False], 2, 5)
print(mutable_list)
mutable_list[0][0] = 10
print(mutable_list)