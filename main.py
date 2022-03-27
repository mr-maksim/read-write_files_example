def read_recipt():

    cook_book = {}
    with open('files/recipt.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dishes = line.strip()
            print(dishes)
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


read_recipt()
