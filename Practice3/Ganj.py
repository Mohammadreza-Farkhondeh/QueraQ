
def search_L(table, i, j):
    count = 0
    for k in range(2, m):
        try:
            if table[-j][-i-k+1] == '*':
                    for z in range(1, (2*k)):
                        if table[-j-z][-i-k+1] != '*':
                            break
                    else:
                        count += 1
        except:
            break

    return count


def main():
    global m, n, Gcount
    m, n = map(int, input().split())
    Gcount = 0

    table = []
    for j in range(m):
        row = list(input())
        table.append(row)

    for j in range(1, m):
        for i in range(1, n):
            if table[-j][-i] == '*':
                Gcount += search_L(table, i, j)

    print(Gcount)


if __name__ == '__main__':
    main()