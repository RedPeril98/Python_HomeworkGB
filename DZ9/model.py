phone_book = []

def open_phone_book():
    with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
        phone_book = data.readlines()
    for contact in phone_book:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1],'comment':contact[2]})
        print('файл открыт')
        return phone_book


def save_phone_book():
    with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
        for i in phone_book:
           data.write(i)

def show_phone_book():
    print(phone_book)
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
            for i in phone_book:
                print(' '.join(i.split(';')))


def add_phone_book():
    if len(phone_book) == 0:
        print('Вы не открыли файл либо файл пуст')
    else:
        user_info = input('Введите данные нового контакта: ')
        user_info = ';'.join(user_info.split(' '))
        phone_book.append('\n' + user_info)


def change_phone_book():
    user_info = input('Введите номенр контакта, которого вы хотите изменить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input('Введите новый номер контакта: ')
            phone_book[i] = phone_book[i].replace(user_info, new_user_info)

def searh_phone_book():
    user_info = input('Введите номер контакта, которого вы хотите найти: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])

def delete_phone_book():
    user_info = input('Введите номер контакта, которого вы хотите удалить: ')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            # question = input('Действительно удалить контакт? у - да, n - нет: ')
            # if question == 'y':
            phone_book.pop(i)
            break


phone_book = open_phone_book()