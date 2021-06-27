number = 123321

n = [str(number)[:3], str(number)[:2:-1]]

if n[0] == n[1]:
    print('Счастливый билет')
else:
    print('Несчастливый билет')
