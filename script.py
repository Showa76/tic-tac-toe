from art import tprint

def meet():
    tprint('TIC-TAC-TOE', font='fuzzy ')
    tprint('  -THE GAME-', font='fuzzy ')
    print('-----------------------')
    print('    Добро пожаловать   ')
    print('          в игру       ')
    print('     крестики-нолики   ')
    print('-----------------------')
    print('  Чтобы  сделать  ход  ')
    print('  введите координаты   ')
    print('    в формате: "x y"   ')
    print('   x - номер строки    ')
    print('   y - номер столбца   ')
    print('         УДАЧИ!        ')
    print('-----------------------')

def show():
    print("  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print(f"{i} | {' | '.join(frame[i])} | ")
        print("---------------")

def ask():
    while True:
        cords = input('      Ваш ход: ').split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Выход за пределы поля!")
            continue

        if frame[x][y] != " ":
            print(" Клетка занята!")
            continue

        return x, y

def check_win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)))

    for cord in win_comb:
        symbols = []
        for c in cord:
            symbols.append(frame[c[0]][c[1]])

        if symbols == ["X", "X", "X"]:
            show()
            print(" ПОБЕДА! ")
            print(" Выиграл X!!!")
            return True

        if symbols == ["O", "O", "O"]:
            show()
            print(" ПОБЕДА! ")
            print(" Выиграл O!!!")
            return True
    return False




count = 0
frame = [[" "] * 3 for i in range(3)]
meet()

while True:

    count += 1
    print(f" Ход номер: {count}")
    show()

    if count % 2 == 1:
        print(' Ходит крестик! ')
    else:
        print(' Ходит нолик! ')

    x, y = ask()

    if count % 2 == 1:
        frame[x][y] = "X"
    else:
        frame[x][y] = "O"

    if check_win():
        break

    if count == 9:
        show()
        print(" Ничья! ")
        break
