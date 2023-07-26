import view
import model

def start():
    while True:
     choice = view.main_menu()
     match choice:
        case 1:
          model.open_phone_book()
          print('Файл открыт')
        case 2:
           model.save_phone_book()
           print('Сохранение...')
        case 3:
           model.show_phone_book()
           print('Контакты показаны выше')
        case 4:
           model.add_phone_book()
           print('Добавление контакта')
        case 5:
           model.change_phone_book()
           print('Изменение контакта')
        case 6:
           model.searh_phone_book()
           print('Поиск контакта')
        case 7:
           model.delete_phone_book()
           print('Удалили контакта')
        case 8:
            print('Выход осуществлен')
            break

       