calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    list_to_search = (len(string), string.upper(), string.lower())
    return print(list_to_search)
def is_contains(string, list_to_search):
    count_calls()
    if string.casefold() in list_to_search.casefold():
        return print(True)
    else:
        return print(False)


string_info('Новый модуль, новые знания')
string_info('Очень жду новогодние праздники')
is_contains('Урбан', 'Новый модуль, новые знания')
is_contains('НОВЫЙ', 'Новый модуль, новые знания')
print(calls)