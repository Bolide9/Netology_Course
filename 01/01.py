phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

print(len(phrase_1), len(phrase_2))

if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
elif len(phrase_1) < len(phrase_2):
    print('Фраза 2 длиннее фразы 1')
else:
    print('Фразы равной длины')
