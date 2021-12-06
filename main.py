# player = {
#     "name": "",
#     "fields": [[], [], [], []],
#     "hits": []
# }
#
# log = {
#     "game": "",
#     "game_mod": "",
#     "player_1": player,
#     "player_2": player,
#     "winner": ""
# }
#
# with open("log.txt", "r", encoding='utf-8') as file:
#     lst = [line.strip() for line in file]
#
# print(lst)
# hits = [lst[i][3:] if lst[i][:3] == "P1:" else "" for i in range(16, len(lst)-2)]
# hits_1 = list(filter(None, hits))
# hits = [lst[i][3:] if lst[i][:3] == "P2:" else "" for i in range(16, len(lst)-2)]
# hits_2 = list(filter(None, hits))
# log["game"] = lst[0][5:]
# log["game_mod"] = lst[1][10:]
# log["player_1"] = {
#     "name": lst[2][3:],
#     "fields": [[lst[6][2:]], [lst[7][2:]], [lst[8][2:]], [lst[9][2:]]],
#     "hits": hits_1
# }
# log["player_2"] = {
#     "name": lst[3][3:],
#     "fields": [[lst[11][2:]], [lst[12][2:]], [lst[13][2:]], [lst[14][2:]]],
#     "hits": hits_2
# }
# log["winner"] = lst[-1]
# print(log)


#
# field = creat_field(11, 11, "art")
# for i in field:
#     print(i)
#
# print("\n\n\n\n")
# field1 = creat_field1(11, 11, 'dima')
# for i in field1:
#     print(i)

#
# Создаем координаты для выстрелов:
def creat_field_empty():
    x = y = 11
    lst = "ABCDEFGHIJ"
    field = [[lst[i - 1] if (j == 0 and i != 0) else "_" for i in range(x)] for j in range(y)]
    for i in range(1, y):
        field[i][0] = i
    field[0][0] = ""
    return field


def creat_field():
    x = y = 11
    lst = "ABCDEFGHIJ"
    field = [[lst[i - 1] if (j == 0 and i != 0) else "_" for i in range(x)] for j in range(y)]
    for i in range(1, y):
        field[i][0] = i
    field[0][0] = ""
    arrangement_ships(field)

    return field


def otrisovka():
    print(f'     <<< {name_1} >>>                                                     <<< {name_2} >>>')
    for i in range(len(field_1_empty)):
        print(f'{field_1_empty[i]}               {field_2_empty[i]}')


def shot(field, name):
    otrisovka()
    koord_x = int(input("Введите координату x: "))
    koord_y = int(input("Введите координату y: "))
    while not all(10 > i > 0 for i in (koord_x, koord_y)):
        print("Введите корректные значения(1-10)")
        koord_x = int(input("Введите координату x: "))
        koord_y = int(input("Введите координату y: "))
    if field[koord_y][koord_x] == "O":
        field[koord_y][koord_x] = "X"
        if name == name_1:
            field_1_empty[koord_y][koord_x] = "X"
        else:
            field_2_empty[koord_y][koord_x] = "X"

        otrisovka()

        print("Вы попали")
        return True
    else:
        field[koord_y][koord_x] = "*"
        if name == name_1:
            field_1_empty[koord_y][koord_x] = "*"
        else:
            field_2_empty[koord_y][koord_x] = "*"
        otrisovka()
        print("Вы не попали")
        return False


def game():
    player1 = False
    player2 = False
    while player1 == False and player2 == False:
        popadanie = True
        while popadanie != False:
            print(f"Введите координату корабля соперника <<< {name_1} >>>")
            popadanie = shot(field_1, name_1)
            if popadanie == True:
                player1 = check_field(field_1)
                if player1 == True:
                    break
                else:
                    continue
        popadanie = True
        while popadanie != False:
            if player1 == True:
                break
            print(f"Введите координату корабля соперника << {name_2} >>>")
            popadanie = shot(field_2, name_2)
            if popadanie == True:
                player2 = check_field(field_2)
                if player2 == True:
                    break
            else:
                continue

    if player1 == True:
        print(f"Победил <<< {name_1} >>>")
    elif player2 == True:
        print(f"Победил <<< {name_2} >>>")


def check_field(field):
    for i in field:
        if i.count("O") != 0:
            return False
    return True


def ships_1(field):
    ship = input(f'Введите однопалубный корабль в формате A1|E1|A6|F10 : ')
    # ship = 'A1|E1|A6|F10'
    coordinates = ship.split('|')
    for i in range(4):
        coordinates[i] = coordinates[i]
        x = coordinates[i][0]
        y = int(coordinates[i][1:])
        column = field[0].index(x)
        row = y
        field[row][column] = 'O'


def ships_2(field):
    ship = input(f'Введите двухпалубные корабли в формате F6_G6|B9_C9|I7_I8 : ')
    # ship = 'F6_G6|B9_C9|I7_I8'
    ship = ship.split('|')
    for l in range(3):
        coordinates = ship[l].split('_')
        for i in range(2):
            coordinates[i] = coordinates[i]
            x = coordinates[i][0]
            y = int(coordinates[i][1:])
            column = field[0].index(x)
            row = y
            field[row][column] = 'O'


def ships_3(field):
    ship = input(f'Введите трехпалубный корабль в формате G2_G4|D5_D7 : ')
    # ship = 'G2_G4|D5_D7'
    ship = ship.split('|')
    for i in range(len(ship)):
        coordinates = ship[i].split('_')
        x1 = coordinates[0][0]
        y1 = int(coordinates[0][1:])
        x2 = coordinates[1][0]
        y2 = int(coordinates[1][1:])
        if x1 == x2:
            column = field[0].index(x1)
            for row in range(y1, y2 + 1):
                field[row][column] = 'O'
        if y1 == y2:
            column1 = field[0].index(x1)
            column2 = field[0].index(x2)
            row = y1
            for column in range(column1, column2 + 1):
                field[row][column] = 'O'


def ships_4(field):
    ship = input(f'Введите четырехплубный корабль в формате B3_E3 : ')
    # ship = 'B3_E3'
    ship = ship.split('|')
    for i in range(len(ship)):
        coordinates = ship[i].split('_')
        x1 = coordinates[0][0]
        y1 = int(coordinates[0][1:])
        x2 = coordinates[1][0]
        y2 = int(coordinates[1][1:])
        if x1 == x2:
            column = field[0].index(x1)
            for row in range(y1, y2 + 1):
                field[row][column] = 'O'
        if y1 == y2:
            column1 = field[0].index(x1)
            column2 = field[0].index(x2)
            row = y1
            for column in range(column1, column2 + 1):
                field[row][column] = 'O'

    # for k in range(11):
    #     print(field[k])


def arrangement_ships(field):
    ships_1(field)
    ships_2(field)
    ships_3(field)
    ships_4(field)
    pass


#################################


def main():
    while True:
        gametype = int(
            input("1.Игрок против игрока\n2. Игрок против ИИ\n3. ИИ против ИИ\n4.Загрузить игру\nВаш выбор:"))
        if gametype == 1:
            global name_1
            global field_1
            global field_1_empty
            name_1 = input("Имя 1:")
            field_1 = creat_field()
            field_1_empty = creat_field_empty()

            global name_2
            global field_2
            global field_2_empty
            name_2 = input("Имя 2:")
            field_2 = creat_field()
            field_2_empty = creat_field_empty()

            game()
        elif gametype == 2:
            print("Данный пункт в разработке :)")
            continue

        elif gametype == 3:
            print("Данный пункт в разработке :)")
            continue

        elif gametype == 4:
            print("Данный пункт в разработке :)")
            continue

        else:
            print("Выход..)")
            break


if __name__ == "__main__":
    main()
