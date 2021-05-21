documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'},
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': [],
}


def func(command):
    if command == 'p':
        doc_number = input('Введите номер документа: ')

        print(get_owner_doc(doc_number))

    if command == 's':
        doc_number = input('Введите номер документа: ')

        print(getShelf(doc_number))

    if command == 'l':
        get_all_info()

    if command == 'ads':
        number = input('Введите номер полки: ')

        print(add_shelf(number))

    if command == 'ds':
        number = input('Введите номер полки: ')

        print(delete_shelf(number))

    if command == 'q':
        ## В jupiter почему-то не работает
        ## также и quit()/quit/exit()/exit
        exit()


def get_owner_doc(docNumber):
    name = None

    for i in documents:

        if docNumber == i['number']:
            name = i['name']

    if name is not None:
        return f'Владелец документа: {name}'

    return 'Результат:\nДокумент не найден в базе'


def get_all_info():
    for _documents in documents:
        for key, value in directories.items():
            if _documents["number"] in value:
                print(
                    f'№: {_documents["number"]}, тип: {_documents["type"]}, владелец: {_documents["name"]}, полка хранения: {key}')


def getShelf(docNumber):
    result = None

    for key, value in directories.items():
        if docNumber in value:
            result = key

    if result is None:
        return 'Результат:\nДокумент не найден в базе'

    return f'Результат: \nДокумент хранится на полке: {result}'


def add_shelf(_number):
    if _number in directories.keys():
        return 'Такая полка уже существует. Текущий перечень полок: ' + ', '.join(
            str(i) for i in directories.keys())
    else:
        directories.update({_number: []})
        return 'Полка добавлена. Текущий перечень полок: ' + ', '.join(str(i) for i in directories.keys())


def delete_shelf(_number):
    if _number in directories.keys() and len(directories.get(_number)) > 0:
        return 'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: ' + ', '.join(
            str(i) for i in directories.keys())
    else:
        if directories.get(_number) is None:
            return 'Такой полки не существует. Текущий перечень полок: ' + ', '.join(
                str(i) for i in directories.keys())

        if len(directories.get(_number)) == 0:
            directories.pop(_number)
            return 'Полка удалена. Текущий перечень полок: ' + ', '.join(str(i) for i in directories.keys())


while True:
    func(command=input('Введите команду: '))


