my_dict = {'Sergey' : 2000, 'Denis' : 1999, 'Evgeny' : 1996, 'Diana' : 2005}
print(my_dict)
print(my_dict['Sergey'])
print(my_dict.get('Anatoly'))
my_dict.update({'Vasiliy' : 1980,
                'Daria' : 1989})
a = my_dict.pop('Denis')
print(a)
print(my_dict)

my_set = {1, 1 , 2, 2, True, 1.5, 3, 1, 8, 'string' , True, False, 1.5}
print(my_set)
my_set.add('milk')
my_set.add(2.98)
my_set.remove(1)
print(my_set)