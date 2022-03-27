from os import system, name
import config


def menu():
    while True:
        print_main_menu()
        while True:
            try:
                choose = int(input('Введите номер нужного пункта: '))
                break
            except:
                print("Вы ввели некорректные данные")
        if choose == 1:
            clear()
            dishes_list(open_recipt(config.RECIPT_PATH))
        elif choose == 2:
            clear()
            print(shop_list())
        elif choose == 3:
            clear()
            print(open_recipt(config.RECIPT_PATH))
        elif choose == 0:
            exit()


def print_main_menu():
    menu_list = ["1 - Просмотр списка блюд", "2 - Получить список покупок",
                 "3 - Вывести словарь 'cook_book'", "0 - Exit"]
    for item in menu_list:
        print(item)


def dishes_list(cook_book):
    for num, item in enumerate(cook_book.keys()):
        print(f'{num + 1}) {item}')
    print('\n')
    menu()


def shop_list():
    clear()
    dishes_list = input(
        "Введите через запятую наименования блюд:\n").split(',')
    person = int(input("Введите количество человек:\n"))
    clear()
    result = get_shop_list_by_dishes(dishes_list, person)
    return result


def get_shop_list_by_dishes(dishes, person):
    result = {}
    cook_book = open_recipt(config.RECIPT_PATH)
    for item in dishes:
        if item in cook_book:
            for ingridient in cook_book[item]:
                if ingridient["ingridient_name"] not in result:
                    result[ingridient["ingridient_name"]] = dict((('measure', str(
                        ingridient["measure"])), ('quantity', ingridient["quantity"] * person)))
                else:
                    result[ingridient["ingridient_name"]] = dict((('measure', str(ingridient["measure"])), ('quantity', str(
                        ((ingridient["quantity"] * person) + result[ingridient["ingridient_name"]]['quantity'])))))
        else:
            print(f'Блюдо "{item}" не найдено')
    return(result)


def open_recipt(recipt_path):
    cook_book = {}
    with open(recipt_path, 'r', encoding='utf-8') as file:
        for line in file:
            dishes = line.strip()
            cook_book[dishes] = []
            quantity = int(file.readline())
            for ingredients in range(quantity):
                line_split = file.readline().strip().split('|')
                cook_book[dishes].append(dict([
                    ('ingridient_name', line_split[0]),
                    ('quantity', int(line_split[1])),
                    ('measure', line_split[2]),
                ]))
            file.readline()
    return cook_book


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    clear()
    menu()
