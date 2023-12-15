user_name_1 = input('Введите имя пользователя: ')
user_name_2 = input('Введите имя пользователя: ')


table = [['-' for _ in range(3)] for _ in range(3)]
print(f'  0 1 2')
print(f'0 {table[0][0]} {table[0][1]} {table[0][2]}')
print(f'1 {table[1][0]} {table[1][1]} {table[1][2]}')
print(f'2 {table[2][0]} {table[2][1]} {table[2][2]}')

def fill_cell(i, j, el):
    table[int(i)][int(j)] = el
    print(f'  0 1 2')
    print(f'0 {table[0][0]} {table[0][1]} {table[0][2]}')
    print(f'1 {table[1][0]} {table[1][1]} {table[1][2]}')
    print(f'2 {table[2][0]} {table[2][1]} {table[2][2]}')


def check_cell(i, j):
    if table[int(i)][int(j)] == '-':
        return True
    else:
        return False


def check_isdigit(i, j):
    if i.isdigit() and j.isdigit() and 0 <= int(i) <= 2 and 0 <= int(j) <= 2:
        return True
    else:
        return False


def check_win():
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if table[i][j] != '-':
                if table[i][j] == 'x':
                    x_count += 1
                else:
                    o_count += 1
            else:
                x_count = 0
                o_count = 0
                break
        if x_count == 3:
            return f'Выиграл игрок {user_name_1}'
        else:
            x_count = 0
        if o_count == 3:
            return f'Выиграл игрок {user_name_2}'
        else:
            o_count = 0

    for i in range(3):
        for j in range(3):
            if table[j][i] != '-':
                if table[j][i] == 'x':
                    x_count += 1
                else:
                    o_count += 1
            else:
                x_count = 0
                o_count = 0
                break
        if x_count == 3:
            return f'Выиграл игрок {user_name_1}'
        else:
            x_count = 0
        if o_count == 3:
            return f'Выиграл игрок {user_name_2}'
        else:
            o_count = 0
    for i in range(3):
        for j in range(3):
            if i - j == 0:
                if table[i][j] != '-':
                    if table[i][j] == 'x':
                        x_count += 1
                    else:
                        o_count += 1
                else:
                    x_count = 0
                    o_count = 0
                    break
        if x_count == 3:
            return f'Выиграл игрок {user_name_1}'
        else:
            x_count = 0
        if o_count == 3:
            return f'Выиграл игрок {user_name_2}'
        else:
            o_count = 0
    for i in range(3):
        for j in range(3):
            if i + j == 2:
                if table[i][j] != '-':
                    if table[i][j] == 'x':
                        x_count += 1
                    else:
                        o_count += 1
                else:
                    x_count = 0
                    o_count = 0
                    break
        if x_count == 3:
            return f'Выиграл игрок {user_name_1}'
        else:
            x_count = 0
        if o_count == 3:
            return f'Выиграл игрок {user_name_2}'
        else:
            o_count = 0


def check_tie():
    s = []
    for i in table:
        s.extend(i)
    if '-' not in s: return 'Tie'
    else: return False

def step_user_name_1():
    print(f'Ход игрока {user_name_1}')
    i = input('Введите 1 координату: ')
    j = input('Введите 2 координату: ')
    if check_isdigit(i, j):
        if check_cell(i, j):
            return fill_cell(i, j, 'x')
        else:
            print('Тут занято, введите заново!')
            return step_user_name_1()
    else:
        print('Введите цифры от 0-2!')
        return step_user_name_1()


def step_user_name_2():
    print(f'Ход игрока {user_name_2}')
    i = input('Введите 1 координату: ')
    j = input('Введите 2 координату: ')
    if check_isdigit(i, j):
        if check_cell(i, j):
            return fill_cell(i, j, 'o')
        else:
            print('Тут занято, введите заново!')
            return step_user_name_2()
    else:
        print('Введите цифры от 0-2!')
        return step_user_name_2()


def game():
    step_user_name_1()
    if check_win():
        return check_win()
    if check_tie():
        return check_tie()
    step_user_name_2()
    if check_win():
        return check_win()
    else:
        return game()


print(game())
