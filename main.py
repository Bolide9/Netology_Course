lst = input('Введите числа: ')
lst = lst.split()
_lst = []

for val in lst:
    value = int(val)
    if lst.count(str(value)) > 1:
        _lst.append(value)

_lst = list(set(_lst))

print(sorted(_lst))