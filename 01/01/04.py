width = 10
length = 205
height = 5

if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif 50 > width > 15 or 50 > length > 15 or 50 > height > 15:
    print('Коробка №2')
elif length > 2:
    print('Упаковка для лыж')
else:
    print('Стандартная коробка №3')

