def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['str', False, 0]
values_dict = {'a' : True, 'b' : 20, 'c' : 'str'}
values_list2 = [20, 'str']
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)