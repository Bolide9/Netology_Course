# Меньше программировать надо)
import calendar as cl

year = int(input())

if cl.isleap(year):
    print('Високосный год')
else:
    print('Обычный год')

