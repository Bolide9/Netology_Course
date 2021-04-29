import math

figure = input('Введите тип фигуры: ').strip().capitalize()

if figure == 'Круг':
    r = int(input('Введите радиус: '))
    s = math.pi * (r * r)
    print(f'Площадь круга: {s}')

elif figure == 'Треугольник':
    a = int(input('Введите длину стороны A: '))
    b = int(input('Введите длину стороны B: '))
    c = int(input('Введите длину стороны C: '))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p-a) * (p-b) * (p-c))
    print(f'Площадь треугольника: {s}')

elif figure == 'Прямоугольник':
    a = int(input('Введите длину стороны A: '))
    b = int(input('Введите длину стороны B: '))
    s = a * b
    print(f'Площадь прямоугольника: {s}')
