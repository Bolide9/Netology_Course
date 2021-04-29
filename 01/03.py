day = int(input('Введите день: '))
month = input('Введите месяц: ')


def get_month_index(_month):
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']
    return months.index(_month) + 1


def get_sign(day, month):
    if (21 <= day <= 31 and month == 3) or (month == 4 and 1 <= day <= 19):
        print("Ваш знак зодиака: Овен")
    elif (20 <= day <= 30 and month == 4) or (month == 5 and 1 <= day <= 20):
        print("Ваш знак зодиака: Телец")
    elif (21 <= day <= 31 and month == 5) or (month == 6 and 1 <= day <= 21):
        print("Ваш знак зодиака: Близнецы")
    elif (22 <= day <= 30 and month == 6) or (month == 7 and 1 <= day <= 22):
        print("Ваш знак зодиака: Рак")
    elif (23 <= day <= 31 and month == 7) or (month == 8 and 1 <= day <= 22):
        print("Ваш знак зодиака: Лев")
    elif (23 <= day <= 31 and month == 8) or (month == 9 and 1 <= day <= 22):
        print("Ваш знак зодиака: Дева")
    elif (23 <= day <= 30 and month == 9) or (month == 10 and 1 <= day <= 23):
        print("Ваш знак зодиака: Весы")
    elif (24 <= day <= 31 and month == 10) or (month == 11 and 1 <= day <= 22):
        print("Ваш знак зодиака: Скорпион")
    elif (23 <= day <= 30 and month == 11) or (month == 12 and 1 <= day <= 21):
        print("Ваш знак зодиака: Стрелец")
    elif (22 <= day <= 31 and month == 12) or (month == 1 and 1 <= day <= 20):
        print("Ваш знак зодиака: Козерог")
    elif (21 <= day <= 31 and month == 1) or (month == 2 and 1 <= day <= 18):
        print("Ваш знак зодиака:Водолей")
    elif (19 <= day <= 29 and month == 2) or (month == 3 and 1 <= day <= 20):
        print("Ваш знак зодиака: Рыбы")


get_sign(day, get_month_index(month))
