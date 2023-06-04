def fill_cell(table, x, y, m):
    table[x][y // b][y % b] = str(m)


def check(table, x, y, m):
    m = str(m)
    for l in table[x]:
        for v in l:
            if v == m:
                return False
    for l in table:
        if l[y // b][y % b] == m:
            return False

    box_row = (x // a) * a
    box_col = (y // b) * b
    for i in range(box_row, box_row + a):
        for j in range(box_col, box_col + b):
            if table[i][j // b][j % b] == m:
                return False
    if table[x][y // b][y % b] != '.':
        return False
    return True


def print_table(table):
    stre = ''
    for hl in table:
        for sl in hl:
            for n in sl:
                stre += str(n)
        stre += '\n'

    return stre.rstrip()


def make_table(a, b):
    table = [[['.' for i in range(b)] for j in range(a)] for k in range(a * b)]
    return table


def main():
    global a, b
    a, b = map(int, input().split())

    Table = make_table(a, b)

    player = 'player 1:'

    q = int(input())

    for qu in range(q):
        x, y, m = map(int, input().split())
        x, y = x - 1, y - 1
        print(player)

        if check(Table, x, y, m):
            fill_cell(Table, x, y, m)
            print(print_table(Table))
            if player == 'player 1:':
                player = 'player 2:'
            else:
                player = 'player 1:'
        else:
            print('invalid move')


if __name__ == '__main__':
    main()
