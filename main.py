from os import system, name
import config


def menu():
    # print(f'{"_"*15}Добро пожаловать{"_"*15}')
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
    elif choose == 0:
        exit()


def print_main_menu():
    menu_list = ["1 - Просмотр списка блюд", "0 - Exit"]
    for item in menu_list:
        print(item)


def dishes_list(cook_book):
    for num, item in enumerate(cook_book.keys()):
        print(f'{num + 1}) {item}')
    print('\n')
    menu()


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
                    ('quantity', line_split[1]),
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
    menu()
